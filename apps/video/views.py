# -*- coding:utf-8 -*-
from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response

from utils.mixin_utils import LoginRequireMixin
from .models import Video
from operation.models import VideoComments

# Create your views here.


class VideoListView(View):
    """
    视频分页
    """
    def get(self, request, category_id):
        if category_id == '1':
            category = 'cy'
            current_nav = 'chuyi'
        elif category_id == '2':
            category = 'sh'
            current_nav = 'shenghuo'
        elif category_id == '3':
            category = 'qs'
            current_nav = 'qiangshen'

        category_id = category_id
        video_lists = Video.objects.filter(category=category).order_by("-add_time")

        # 关键词搜索功能
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_courses = video_lists.filter(
                Q(name__icontains=search_keywords) | Q(desc__icontains=search_keywords) | Q(
                    detail__icontains=search_keywords))
        # name__icontains django会把name转换为like语句
        # django的model中，出现了i，则不区分大小写

        sort = request.GET.get('sort', '')
        if sort:
            # 参与人数
            if sort == "students":
                video_lists = video_lists.order_by("-students")
            # 最热门
            if sort == "hot":
                video_lists = video_lists.order_by("-click_nums")

        # 课程列表分页
        try:
            page = request.GET.get('page', '1')
        except PageNotAnInteger:
            page = 1
        p = Paginator(video_lists, 9, request=request)
        video_lists = p.page(page)

        # 热门推荐 即点击量
        hot_video = Video.objects.filter(category=category).order_by("click_nums")[:3]
        # return render_to_response('video-list.html', locals())
        return render(request, 'video-list.html', locals())


class VideoDetailView(LoginRequireMixin,View):
    """
    课程详情页展示.
    """
    def get(self, request, video_id):
        video_detail = Video.objects.get(id=video_id)
        # 增加课程点击数 v
        video_detail.click_nums = F('click_nums') + 1
        video_detail.save()

        # 评论
        all_comments = VideoComments.objects.filter(video=video_id)
        # 验证用户是否登录
        has_course_fav = False
        has_org_fav = False

        # 推荐相关课程
        tag = video_detail.tag
        if tag:
            relate_course = Video.objects.filter(tag=tag).order_by('?')[:1]
        else:
            relate_course = []

        return render(request, 'video-detail.html', locals())


class VideoCommentsView(LoginRequireMixin,View):
    """
    跳转评论页
    """
    def get(self, request, course_id):
        # 视频详情
        course = Video.objects.get(id=course_id)
        # 视频评论
        all_comments = VideoComments.objects.filter(course=course_id)

        return render(request, 'course-comment.html', locals())


class AddCommentView(LoginRequireMixin, View):

    """
    添加评论
    """

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}'
                                , content_type='application/json')
        video_id = request.POST.get("video_id", 0)
        comments = request.POST.get("comments", '')
        if video_id > 0 and comments:
            video_comment = VideoComments()
            #  由于在CourseComments里面course是外键，保存添加的应该是一个类
            video = Video.objects.get(id=video_id)
            video_comment.course = video
            video_comment.user = request.user
            video_comment.comments = comments
            video_comment.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


class VideoVideo(View):
    """
    视频播放
    """

    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        return render(request, 'video_video.html', locals())


class VideoSearch(View):
    """
    搜索
    """

    def get(self, request, category_id):
        video_name = request.GET.get('keywords', '')
        # if video_name is None:
        #     return HttpResponse('{"status":"fail", "msg":"搜索框为空"}', content_type='application/json')
        # video = Video()
        video_search_lists = Video.objects.filter(Q(name__icontains=video_name) |
                                                  Q(desc__icontains=video_name) |
                                                  Q(detail__icontains=video_name)).order_by('?')[:9]
        if category_id == '1':
            category = 'cy'
            current_nav = 'chuyi'
        elif category_id == '2':
            category = 'sh'
            current_nav = 'shenghuo'
        elif category_id == '3':
            category = 'qs'
            current_nav = 'qiangshen'

        # 课程列表分页
        try:
            page = request.GET.get('page', '1')
        except PageNotAnInteger:
            page = 1
        p = Paginator(video_search_lists, 9, request=request)
        video_lists = p.page(page)
        return render(request, 'video-list.html', locals())
