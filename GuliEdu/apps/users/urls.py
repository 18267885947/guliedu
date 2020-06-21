from django.conf.urls import url
from users.views import IndexView,UserRegister,UserLogin,user_logout,user_active,user_forget,user_reset,user_info,user_changeimage,user_changeinfo,password_reset,user_changeemail,user_resetemail,user_course,user_love,user_message,user_deletemessage


urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^user_register$',UserRegister.as_view(),name='user_register'),
    url(r'^user_login$',UserLogin.as_view(),name='user_login'),
    url(r'^user_logout$',user_logout,name='user_logout'),
    url(r'^user_active/(\w+)/$',user_active,name='user_active'),
    url(r'^user_forget$',user_forget,name='user_forget'),
    url(r'^user_reset/(\w+)/$',user_reset,name='user_reset'),
    url(r'^user_info/',user_info,name='user_info'),
    url(r'^user_changeimage/', user_changeimage, name='user_changeimage'),
    url(r'^user_changeinfo/', user_changeinfo, name='user_changeinfo'),
    url(r'^password_reset/', password_reset, name='password_reset'),
    url(r'^user_changeemail/', user_changeemail, name='user_changeemail'),
    url(r'^user_resetemail/', user_resetemail, name='user_resetemail'),
    url(r'^user_course/', user_course, name='user_course'),
    url(r'^user_love/', user_love, name='user_love'),
    url(r'^user_message/', user_message, name='user_message'),
    url(r'^user_deletemessage/', user_deletemessage, name='user_deletemessage'),
]