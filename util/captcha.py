from django.core.signing import TimestampSigner
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import time
import os


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
                         fontPath="/static/other/DroidSansFallback.ttf", fontSize=36):
        source = list(string.digits + string.ascii_letters)
        captcha = random.sample(source, captchaLen)
        image = Image.new("RGB", (width, height), (255, 255, 255))
        font = ImageFont.truetype(fontPath, fontSize)
        draw = ImageDraw.Draw(image)

        for x in range(0, width):
            for y in range(0, height):
                draw.point((x, y), fill=self._randomColor(64, 255))

        charWidth = width / captchaLen
        for i in range(0, captchaLen):
            beginX = charWidth * i + random.randint(0, charWidth - fontSize)
            beginY = random.randint(0, height - fontSize)
            draw.text((beginX, beginY), captcha[i], font=font, fill=self._randomColor(32, 127))

        image = image.filter(ImageFilter.BLUR)

        captchaPath = os.path.normcase(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/static/images/captcha/captcha.png")
        image.save(captchaPath, "png")

        return {"captchaImagePath": captchaPath, "captcha": ''.join(captcha)}

    def _randomColor(self, rangeLow, rangeHigh):
        return (
            random.randint(rangeLow, rangeHigh), random.randint(rangeLow, rangeHigh),
            random.randint(rangeLow, rangeHigh))
