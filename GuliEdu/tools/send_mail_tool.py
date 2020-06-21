from users.models import EmailVerifyCode
from random import choice,randrange
from django.core.mail import send_mail
from GuliEdu.settings import EMAIL_FROM

def get_random_code(code_length):
    code_source='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code=''
    for i in range(code_length):
        str=code_source[randrange(0,len(code_source)-1)]
        code+=str
    return code

def send_mail_code(email,send_type):
    #第一步：创建
    code=get_random_code(8)
    a=EmailVerifyCode()
    a.email=email
    a.send_type=send_type
    a.code=code
    a.save()
    #第二步:正式发送邮件
    send_title=''
    send_body=''
    if send_type==1:
        send_title = '欢迎注册谷粒教育网站'
        send_body = '请点击以下链接进行激活您的账户：\n http://127.0.0.1:8000/user_active/' + code
        send_mail(send_title,send_body,EMAIL_FROM,[email])
    if send_type==2:
        send_title = '谷粒教育重置密码系统'
        send_body = '请点击以下链接进行重置密码：\n http://127.0.0.1:8000/user_reset/' + code
        send_mail(send_title, send_body, EMAIL_FROM, [email])
    if send_type==3:
        send_title = '谷粒教育修改邮箱验证码'
        send_body = '您的验证码是：' + code
        send_mail(send_title, send_body, EMAIL_FROM, [email])










