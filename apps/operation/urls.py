# -*- coding:utf-8 -*-
from django.conf.urls import url

__author__ = '@Able.Tiger'
__date__ = '2018/3/26 16:01'

from .views import AddFavView

urlpatterns = [
	# 用户机构收藏
	url(r'^add_org_fav/$', AddFavView.as_view(), name='add_org_fav'),

]

