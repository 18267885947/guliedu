from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import CourseInfo
import django
# Create your models here.
class UserAsk(models.Model):
    name=models.CharField(max_length=30,verbose_name='姓名')
    phone=models.CharField(max_length=11,verbose_name='电话')
    course=models.CharField(max_length=20,verbose_name='课程')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='资讯信息'
        verbose_name_plural=verbose_name

class UserLove(models.Model):
    love_man=models.ForeignKey(UserProfile,verbose_name='收藏用户',on_delete=models.CASCADE)
    love_id=models.IntegerField(verbose_name='收藏')
    love_type=models.IntegerField(choices=((1,'org'),(2,'course'),(3,'teacher')),verbose_name='收藏类型')
    love_status=models.BooleanField(default=False,verbose_name='收藏状态')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.love_man.email
    class Meta:
        verbose_name='收藏信息'
        verbose_name_plural=verbose_name


class UserCourse(models.Model):
    study_man=models.ForeignKey(UserProfile,verbose_name='学习用户',on_delete=models.CASCADE)
    study_course=models.ForeignKey(CourseInfo,verbose_name='学习课程',on_delete=models.CASCADE)
    add_time=models.DateTimeField(default=django.utils.timezone.now,verbose_name='添加时间')

    def __str__(self):
        return self.study_man.username
    class Meta:
        unique_together=('study_man','study_course')
        verbose_name='用户学习课程信息'
        verbose_name_plural=verbose_name

class UserComment(models.Model):
    comment_man = models.ForeignKey(UserProfile, verbose_name='学习用户',on_delete=models.CASCADE)
    comment_course = models.ForeignKey(CourseInfo, verbose_name='学习课程',on_delete=models.CASCADE)
    comment_content=models.CharField(max_length=300,verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    def __str__(self):
        return self.comment_content
    class Meta:
        verbose_name='用户评论课程信息'
        verbose_name_plural=verbose_name

class UserMessage(models.Model):
    message_man=models.IntegerField(default=0,verbose_name='消息用户')
    message_content=models.CharField(max_length=200,verbose_name='消息内容')
    message_status=models.BooleanField(default=False,verbose_name='消息状态')
    add_time=models.DateTimeField(verbose_name='添加时间',default=django.utils.timezone.now)
    def __str__(self):
        return self.comment_content
    class Meta:
        verbose_name='用户消息信息'
        verbose_name_plural=verbose_name