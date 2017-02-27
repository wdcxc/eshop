import io
import os
import random
import string

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.core.signing import TimestampSigner


class Captcha(object):
    def __init__(self, maxAge=300):
        self.maxAge = maxAge

    def geneCaptchaCode(self, app, action):
        timeSigner = TimestampSigner(salt=app)
        captcha = timeSigner.sign(action)
        return captcha

    def validateCode(self, app, action, captcha):
        timeSigner = TimestampSigner(salt=app)
        try:
            if action == timeSigner.unsign(captcha, self.maxAge):
                return True
        except Exception:
            pass
        return False

    def geneCaptchaImage(self, width=300, height=60, captchaLen=4,
                         fontPath="/static/font/DroidSansFallback.ttf", fontSize=50):
        source = list(string.digits + string.ascii_letters)
        captchaCode = random.sample(source, captchaLen)
        image = Image.new("RGB", (width, height), (255, 255, 255))
        fontPath = os.path.dirname(os.path.dirname(__file__))+fontPath
        font = ImageFont.truetype(os.path.normpath(fontPath), fontSize)
        draw = ImageDraw.Draw(image)

        for x in range(0, width):
            for y in range(0, height):
                draw.point((x, y), fill=self._randomColor(64, 255))

        charWidth = width / captchaLen
        for i in range(0, captchaLen):
            beginX = charWidth * i + random.randint(0, charWidth - fontSize)
            beginY = random.randint(0, height - fontSize)
            draw.text((beginX, beginY), captchaCode[i], font=font, fill=self._randomColor(32, 127))

        image = image.filter(ImageFilter.BLUR)

        # captchaPath = os.path.normcase(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/static/images/captcha/captcha.png")
        captchaImageBuff = io.BytesIO()
        image.save(captchaImageBuff, "png")

        return {"captchaImageBuff": captchaImageBuff.getvalue(), "captchaCode": ''.join(captchaCode).lower()}

    def _randomColor(self, rangeLow, rangeHigh):
        return (
            random.randint(rangeLow, rangeHigh), random.randint(rangeLow, rangeHigh),
            random.randint(rangeLow, rangeHigh))
