import xadmin
from users.models import BannerInfo,EmailVerifyCode
class BannerInfoXadmin(object):
    list_display=['image','url','add_time']


class EmailVerifyCodeXadmin(object):
    list_display=['code','email','send_type','add_time']

xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)