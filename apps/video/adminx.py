# -*- coding:utf-8 -*-
__author__ = '@Able.Tiger'
__date__ = '2018/3/26 14:46'

import xadmin

from .models import Video, CourseCategory


class VideoAdmin(object):
    list_display = ['name', 'category', 'video', "video_url", 'desc', 'detail', 'degree', 'students', 'fav_nums', 'learn_times', 'image',
                    'click_nums', 'add_time']
    search_fields = ['name', 'category', 'video', "video_url", 'desc', 'detail', 'degree', 'students', 'fav_nums', 'learn_times', 'image',
                     'click_nums']
    list_filter = ['name', 'category', 'video', "video_url", 'desc', 'detail', 'degree', 'students', 'fav_nums', 'learn_times', 'image',
                   'click_nums', 'add_time']


class CourseCategoryAdmin(object):
    list_display = ['name', 'add_time', ]
    search_fields = ['name', ]
    list_filter = ['name', 'add_time', ]


xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseCategory, CourseCategoryAdmin)