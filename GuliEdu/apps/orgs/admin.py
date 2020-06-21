from django.contrib import admin
from orgs.models import OrgInfo,CityInfo,TeacherInfo
# Register your models here.
admin.site.register(CityInfo)
admin.site.register(OrgInfo)
admin.site.register(TeacherInfo)
