# -*- coding:utf-8 -*-
__author__ = '@Able.Tiger'
__date__ = '2018/3/26 16:01'
from django.conf.urls import url

from .views import VideoListView, VideoDetailView, VideoCommentsView, AddCommentView, VideoVideo, VideoSearch


urlpatterns = [
	# 视频列表页
	url(r'^video_list/(?P<category_id>\d+)/$', VideoListView.as_view(), name="video_list"),
	# 视频详情页
	url(r'^video_detail/(?P<video_id>\d+)/$', VideoDetailView.as_view(), name="video_detail"),
	# 视频评论也
	url(r'^course_comment/(?P<course_id>\d+)/$', VideoCommentsView.as_view(), name="course_comment"),
	# 添加评论
	url(r'^add_comment/$', AddCommentView.as_view(), name="add_comment"),
	# 视屏播放页
	url(r'^video_video/(?P<video_id>\d+)/$', VideoVideo.as_view(), name="video_video"),
	#搜索
	url(r'^list/(?P<category_id>\d+)/$', VideoSearch.as_view(), name="list"),

]



