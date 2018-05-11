# -*- coding:utf-8 -*-
__author__ = '@Able.Tiger'
__date__ = '2018/3/26 14:41'


import xadmin

from .models import UserAsk, VideoComments, UserFavorite, UserMessage, UserVideo, UserUploadVideo


class UserAskAdmin(object):
	list_display = ['name', 'mobile', 'video_name', ]
	search_fields = ['name', 'mobile', 'video_name', ]
	list_filter = ['name', 'mobile', 'video_name', ]


class VideoCommentsAdmin(object):
	list_display = ['user', 'video', 'comments', 'add_time', ]
	search_fields = ['user', 'video', 'comments', ]
	list_filter = ['user', 'video', 'comments', 'add_time', ]


class UserFavoriteAdmin(object):
	list_display = ['user', 'fav_id', 'fav_type', 'add_time', ]
	search_fields = ['user', 'fav_id', 'fav_type', ]
	list_filter = ['user', 'fav_id', 'fav_type', 'add_time', ]


class UserMessageAdmin(object):
	list_display = ['user', 'message', 'has_read', 'add_time', ]
	search_fields = ['user', 'message', 'has_read', ]
	list_filter = ['user', 'message', 'has_read', 'add_time', ]


class UserVideoAdmin(object):
	list_display = ['user', 'video', 'add_time', ]
	search_fields = ['user', 'video', ]
	list_filter = ['user', 'video', 'add_time', ]


class UserUploadVideoAdmin(object):
	list_display = ['user', 'video', 'add_time', ]
	search_fields = ['user', 'video', ]
	list_filter = ['user', 'video', 'add_time', ]


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(VideoComments, VideoCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserVideo, UserVideoAdmin)
xadmin.site.register(UserUploadVideo, UserUploadVideoAdmin)




