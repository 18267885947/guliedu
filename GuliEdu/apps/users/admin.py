from django.contrib import admin
from users.models import UserProfile,BannerInfo,EmailVerifyCode

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BannerInfo)
admin.site.register(EmailVerifyCode)