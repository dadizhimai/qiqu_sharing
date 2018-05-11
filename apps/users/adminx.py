# -*- coding:utf-8 -*-

__author__ = '@Able.Tiger'
__date__ = '2018/3/26 11:41'

import xadmin

from users.models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
	enable_themes = True  # 使用主题功能，默认为false
	use_bootswatch = True  # 调出主题菜单，默认为false


class GlobalSetting(object):
	site_title = "'奇趣'知识共享后台管理系统"  # 左上角的标题
	site_footer = "奇趣知识共享"  # 底部的标题
	menu_style = "accordion"   # 菜单栏收缩


class EmailVerifyRecordAdmin(object):
	list_display = ['code', 'email', 'send_type', 'send_time']
	search_fields = ['code', 'email', 'send_type']
	list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
	list_display = ['title', 'image', 'url', 'index', 'add_time']
	search_fields = ['title', 'image', 'url', 'index']
	list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

