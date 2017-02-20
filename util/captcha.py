from django.core.signing import TimestampSigner


class Captcha(object):
    def __init__(self, maxAge=300):
        self.maxAge = maxAge

    def geneCaptcha(self, app, action):
        timeSigner = TimestampSigner(salt=app)
        captcha = timeSigner.sign(action)
        return captcha

    def validate(self, app, action, captcha):
        timeSigner = TimestampSigner(salt=app)
        try:
            if captcha == timeSigner.unsign(action, self.maxAge):
                return True
        except Exception:
            pass
        return False
