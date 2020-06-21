from django.shortcuts import render
from courses.models import CourseInfo
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from operations.models import UserLove,UserCourse
from django.db.models import Q
from tools.decorators import login_decorator


def course_list(request):
    all_courses=CourseInfo.objects.all().order_by('id')
    recomment_courses=all_courses.order_by('-add_time')[:3]
    #全局搜索功能的过滤
    keyword=request.GET.get('keyword','')
    if keyword:
        all_courses = CourseInfo.objects.filter(Q(name__icontains=keyword)|Q(desc__icontains=keyword)|Q(detail__icontains=keyword)).order_by()
    sort=request.GET.get('sort','')
    if sort:
        all_courses=all_courses.order_by('-'+sort)
    # 分页功能
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_courses, 2)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'courses/course-list.html',{'all_courses':all_courses,
                                                      'pages':pages,
                                                      'recomment_courses':recomment_courses,
                                                      'sort':sort,
                                                      'keyword':keyword})

def course_detail(request,course_id):
    if course_id:
        course=CourseInfo.objects.filter(id=int(course_id))[0]
        relate_courses=CourseInfo.objects.filter(category=course.category).exclude(id=int(course_id))[:2]
        course.click_num+=1
        course.save()
        #lovecourse和loveorg用来存储用户收藏这个东西的状态，在模板中根据这个状态来确定页面
        lovecourse=False
        loveorg=False
        if request.user.is_authenticated:
            love=UserLove.objects.filter(love_id=int(course_id),love_type=2,love_status=True,love_man=request.user)
            if love:
                lovecourse=True
            love1=UserLove.objects.filter(love_id=course.orginfo.id,love_type=1,love_status=True,love_man=request.user)
            if love1:
                loveorg=True
        return render(request,'courses/course-detail.html',{'course':course,
                                                            'relate_courses':relate_courses,
                                                            'lovecourse':lovecourse,
                                                            'loveorg':loveorg})

@login_decorator
def course_video(request,course_id):
    if course_id:
        course=CourseInfo.objects.filter(id=int(course_id))[0]
        usercourse_list=UserCourse.objects.filter(study_man=request.user,study_course=course)
        if not usercourse_list:
            a=UserCourse()
            a.study_man=request.user
            a.study_course=course
            a.save()
            course.study_num+=1
            course.save()
            usercourse_list=UserCourse.objects.filter(study_man=request.user)
            course_list=[usercourse.study_course for usercourse in usercourse_list]
            org_list=list(set([course.orginfo for course in course_list]))
            if course.orginfo not in org_list:
                course.orginfo.study_num+=1
                course.orginfo.save()
        usercourse_list=UserCourse.objects.filter(study_course=course)
        user_list=[usercourse.study_man for usercourse in usercourse_list]
        usercourse_list=UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        course_list=list(set([usercourse.study_course for usercourse in usercourse_list]))
        return render(request,'courses/course-video.html',{'course':course,
                                                           'course_list':course_list})

def course_comment(request,course_id):
    if course_id:
        course=CourseInfo.objects.filter(id=int(course_id))[0]
        all_comments=course.usercomment_set.all()[:10]
        usercourse_list=UserCourse.objects.filter(study_course=course)
        user_list=[usercourse.study_man for usercourse in usercourse_list]
        usercourse_list=UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        course_list=list(set([usercourse.study_course for usercourse in usercourse_list]))
        return render(request,'courses/course-comment.html',{'course':course,
                                                             'all_comments':all_comments,
                                                             'course_list':course_list})
