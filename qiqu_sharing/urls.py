# -*- coding:utf-8 -*-
"""qiqu_sharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPasswordView, PwdResetView, ModifyPwdView, LogoutView, Index


urlpatterns = [
	url(r'^xadmin/', xadmin.site.urls),
	# url(r'^admin/', admin.site.urls),

	# 登录注册退出找回密码
	# url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
	url(r'^$', Index.as_view(), name='index'),
	url(r'^login/$', LoginView.as_view(), name="login"),
	url(r'^logout/$', LogoutView.as_view(), name="logout"),
	url(r'^register/$', RegisterView.as_view(), name="register"),
	url(r'^captcha/', include('captcha.urls')),
	url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active'),
	url(r'^pwd_reset/(?P<reset_code>.*)/$', PwdResetView.as_view(), name='reset_pwd'),
	url(r'^forget/$', ForgetPasswordView.as_view(), name='forget_pwd'),
	url(r'^modify/$', ModifyPwdView.as_view(), name='modify'),

	# 课程相关配置
	url(r'^video/', include('video.urls', namespace="video")),

	# 用户
	url(r'^users/', include('users.urls', namespace="users")),
	# 用户操作
	url(r'^fav/', include('operation.urls', namespace="operation")),

	# 配置文件上传的访问处理函数
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
