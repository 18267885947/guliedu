from django.contrib import admin
from operations.models import UserCourse,UserAsk,UserMessage,UserLove,UserComment

# Register your models here.
admin.site.register(UserCourse)
admin.site.register(UserAsk)
admin.site.register(UserMessage)
admin.site.register(UserLove)
admin.site.register(UserComment)
