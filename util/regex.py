import re


class Regex(object):
    def validateUsername(self,username, minLength=6, maxLength=30):
        pattern = "[0-9a-zA-Z`~!@#$%^&*()-_=+\[\{\]\}\\\|;:,<\.>/\?]{" + str(minLength) + "," + str(maxLength) + "}"
        if re.match(pattern, username) is None:
            return False
        return True

    def validatePassword(self,password, minLength=8, maxLength=30):
        pattern = "[0-9a-zA-Z`~!@#$%^&*()-_=+\[\{\]\}\\\|;:,<\.>/\?]{" + str(minLength) + "," + str(maxLength) + "}"
        if re.match(pattern, password) is None:
            return False
        return True

    def validateMobile(self,mobile):
        pattern = "1[0-9]{10}"
        if re.match(pattern,mobile) is None:
            return False
        return True

    def validateEmail(self,email):
        pattern = "[0-9a-zA-Z\.]*@[0-9a-zA-Z\.]"
        if re.match(pattern,email) is None:
            return False
        return True
