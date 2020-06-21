from django.shortcuts import render
from orgs.models import OrgInfo,TeacherInfo,CityInfo
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from operations.models import UserLove
from django.db.models import Q

# Create your views here.
def org_list(request):
    all_orgs=OrgInfo.objects.all()
    all_citys=CityInfo.objects.all()
    sort_orgs=all_orgs.order_by('-love_num')[:3]
    #全局搜索功能的过滤
    keyword=request.GET.get('keyword','')
    if keyword:
        all_orgs = OrgInfo.objects.filter(Q(name__icontains=keyword)|Q(desc__icontains=keyword)|Q(detail__icontains=keyword))
    #按照机构类别进行过滤筛选
    cate=request.GET.get('cate','')
    if cate:
        all_orgs=all_orgs.filter(category=cate).order_by()
    #按照机构类别进行过滤筛选
    cityid=request.GET.get('cityid','')
    if cityid:
        all_orgs=all_orgs.filter(cityinfo_id=int(cityid)).order_by()
    #排序
    sort=request.GET.get('sort','')
    if sort:
        all_orgs=all_orgs.order_by('-'+sort)
    #分页功能
    pagenum=request.GET.get('pagenum','')
    pa=Paginator(all_orgs,3)
    try:
        pages=pa.page(pagenum)
    except PageNotAnInteger:
        pages=pa.page(1)
    except EmptyPage:
        pages=pa.page(pa.num_pages)
    return render(request,'orgs/org-list.html',{'all_orgs':all_orgs,
                                                'all_citys':all_citys,
                                                'sort_orgs':sort_orgs,
                                                'pages':pages,
                                                'cate':cate,
                                                'cityid':cityid,
                                                'sort':sort,
                                                'keyword':keyword})

def org_detail(request,org_id):
    if org_id:
        org=OrgInfo.objects.filter(id=int(org_id))[0]
        org.click_num+=1
        org.save()
        lovestatus=False
        if request.user.is_authenticated:
            love=UserLove.objects.filter(love_man=request.user,love_id=int(org_id),love_type=1,love_status=True)
            if love:
                lovestatus=True
        return render(request,'orgs/org-detail-homepage.html',{'org':org,
                                                               'detail_type':'home',
                                                               'lovestatus':lovestatus})

def org_detail_course(request,org_id):
    if org_id:
        org=OrgInfo.objects.filter(id=int(org_id))[0]
        all_courses=org.courseinfo_set.all()
        lovestatus = False
        if request.user.is_authenticated:
            love=UserLove.objects.filter(love_man=request.user,love_id=int(org_id),love_type=1,love_status=True)
            if love:
                lovestatus=True
        # 分页功能
        pagenum = request.GET.get('pagenum', '')
        pa = Paginator(all_courses,2)
        try:
            pages = pa.page(pagenum)
        except PageNotAnInteger:
            pages = pa.page(1)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        return render(request,'orgs/org-detail-course.html',{'org':org,
                                                             'pages':pages,
                                                             'detail_type':'course',
                                                             'lovestatus':lovestatus})

def org_detail_desc(request,org_id):
    if org_id:
        org=OrgInfo.objects.filter(id=int(org_id))[0]
        lovestatus = False
        if request.user.is_authenticated:
            love=UserLove.objects.filter(love_man=request.user,love_id=int(org_id),love_type=1,love_status=True)
            if love:
                lovestatus=True
        return render(request,'orgs/org-detail-desc.html',{'org':org,
                                                           'detail_type':'desc',
                                                           'lovestatus':lovestatus})

def org_detail_teacher(request,org_id):
    if org_id:
        org=OrgInfo.objects.filter(id=int(org_id))[0]
        lovestatus = False
        if request.user.is_authenticated:
            love=UserLove.objects.filter(love_man=request.user,love_id=int(org_id),love_type=1,love_status=True)
            if love:
                lovestatus=True
        return render(request,'orgs/org-detail-teachers.html',{'org':org,
                                                               'detail_type':'teacher',
                                                               'lovestatus':lovestatus})

def teacher_list(request):
    all_teachers=TeacherInfo.objects.all().order_by('id')
    sort_teachers=all_teachers.order_by('-love_num')[:2]
    #全局搜索功能的过滤
    keyword=request.GET.get('keyword','')
    if keyword:
        all_teachers = all_teachers.filter(name__icontains=keyword)

    sort=request.GET.get('sort','')
    if sort:
        all_teachers=all_teachers.order_by('-'+sort)
    # 分页功能
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_teachers, 2)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'orgs/teachers-list.html', {'all_teachers':all_teachers,
                                                       'sort_teachers':sort_teachers,
                                                       'pages':pages,
                                                       'sort':sort,
                                                       'keyword':keyword})

def teacher_detail(request,teacher_id):
    if teacher_id:
        teacher=TeacherInfo.objects.filter(id=int(teacher_id))[0]
        all_teachers = TeacherInfo.objects.all()
        sort_teachers = all_teachers.order_by('-love_num')[:2]
        teacher.click_num+=1
        teacher.save()
        loveteacher=False
        loveorg=False
        if request.user.is_authenticated:
            love=UserLove.objects.filter(love_id=int(teacher_id),love_type=3,love_status=True,love_man=request.user)
            if love:
                loveteacher=True
            love1=UserLove.objects.filter(love_id=teacher.work_company.id,love_type=1,love_status=True,love_man=request.user)
            if love1:
                loveorg=True
        return render(request,'orgs/teacher-detail.html',{'teacher':teacher,
                                                          'sort_teachers':sort_teachers,
                                                          'loveteacher':loveteacher,
                                                          'loveorg':loveorg})