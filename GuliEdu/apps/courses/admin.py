from django.contrib import admin
from courses.models import CourseInfo,LessonInfo,Video,SourceInfo

# Register your models here.
admin.site.register(CourseInfo)
admin.site.register(LessonInfo)
admin.site.register(Video)
admin.site.register(SourceInfo)