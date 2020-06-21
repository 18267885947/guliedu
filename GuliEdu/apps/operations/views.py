from django.shortcuts import render
from operations.forms import UserAskForm,UserCommentForm
from operations.models import UserAsk,UserLove,UserComment
from django.http import JsonResponse
from orgs.models import OrgInfo,TeacherInfo
from courses.models import CourseInfo

# Create your views here.
def user_ask(request):
    user_ask_form=UserAskForm(request.POST)
    if user_ask_form.is_valid():
        user_ask_form.save(commit=True)
        return JsonResponse({'status':'ok','msg':'咨询成功'})
    else:
        return JsonResponse({'status':'fail','msg':'咨询失败'})

def user_love(request):
    loveid=request.GET.get('loveid','')
    lovetype=request.GET.get('lovetype','')
    if loveid and lovetype:
        obj=None
        if int(lovetype)==1:
            obj=OrgInfo.objects.filter(id=int(loveid))[0]
        if int(lovetype)==2:
            obj=CourseInfo.objects.filter(id=int(loveid))[0]
        if int(lovetype) == 3:
            obj = TeacherInfo.objects.filter(id=int(loveid))[0]
        love=UserLove.objects.filter(love_id=int(loveid),love_type=int(lovetype),love_man=request.user)
        if love:
            if love[0].love_status:
                love[0].love_status=False
                love[0].save()
                obj.love_num-=1
                obj.save()
                return JsonResponse({'status':'ok','msg':'收藏'})
            else:
                love[0].love_status = True
                love[0].save()
                obj.love_num+=1
                obj.save()
                return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
        else:
            #如果之前没有收藏过这个东西，那么代表着表中没有这个标记，所以，我们需要县创建这个记录对象，然后把这个记录的状态改为True
            a=UserLove()
            a.love_man=request.user
            a.love_id=int(loveid)
            a.love_type=int(lovetype)
            a.love_status=True
            a.save()
            obj.love_num+=1
            obj.save()
            return JsonResponse({'status':'ok','msg':'取消收藏'})
    else:
        return JsonResponse({'status':'fail','msg':'收藏'})

def user_comment(request):
    user_comment_form=UserCommentForm(request.POST)
    if user_comment_form.is_valid():
        course=user_comment_form.cleaned_data['course']
        content=user_comment_form.cleaned_data['content']
        a=UserComment()
        a.comment_man=request.user
        a.comment_content=content
        a.comment_course_id=course
        a.save()
        return JsonResponse({'status':'ok','msg':'评论成功'})
    else:
        return JsonResponse({'status':'fail','msg':'评论失败'})



def user_deletelove(request):
    loveid=request.GET.get('loveid','')
    lovetype=request.GET.get('lovetype','')
    if loveid and lovetype:
        love=UserLove.objects.filter(love_id=int(loveid),love_type=int(lovetype),love_man=request.user,love_status=True)
        if love:
            love[0].love_status=False
            love[0].save()
            return JsonResponse({'status':'ok','msg':'取消成功'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '取消失败'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '取消失败'})














