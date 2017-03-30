import os
from datetime import datetime

from django.conf import settings


class Upload(object):
    @staticmethod
    def uploadImg(img, dir):
        """上传图片"""
        allowUploadType = ("image/jpg", "image/jpeg", "image/png", "image/gif")
        if img.content_type not in allowUploadType:
            result = {"code": 4, "msg": "上传文件格式错误", "data": {"imagetype": img.content_type}}
        elif img.size >= 10 * 1024 * 1024:
            result = {"code": 4, "msg": "上传文件过大", "data": {"imagesize": img.size}}
        else:
            curdate = datetime.strftime(datetime.date(datetime.now()), "%Y%m%d")
            imgSaveDir = os.path.normpath(settings.BASE_DIR + settings.MEDIA_ROOT + "/" + dir + "/" + curdate)
            if not os.path.exists(imgSaveDir):
                os.makedirs(imgSaveDir)
            fileName = str(datetime.timestamp(datetime.now())) + '_' + img.name
            imgSavePath = os.path.normpath(imgSaveDir + "/" + fileName)
            with open(imgSavePath, "wb") as destination:
                for chunk in img.chunks():
                    destination.write(chunk)
            result = {"code": 200, "msg": "上传文件成功",
                      "data": {"imgUrl": dir + "/" + curdate + "/" + fileName}}
        return result
