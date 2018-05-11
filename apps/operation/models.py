# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from users.models import UserProfile
from video.models import Video
from datetime import datetime


# Create your models here.
class UserAsk(models.Model):
	name = models.CharField(max_length=20, verbose_name=u"姓名")
	mobile = models.CharField(max_length=11, verbose_name=u"手机")
	video_name = models.CharField(max_length=50, verbose_name=u"视频名")

	class Meta:
		verbose_name = u"用户咨询"
		verbose_name_plural = verbose_name


class VideoComments(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name=u"用户")
	video = models.ForeignKey(Video, verbose_name=u"视频")
	comments = models.CharField(max_length=200, verbose_name=u"评论")
	add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"视频评论"
		verbose_name_plural = verbose_name


class UserFavorite(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name=u"用户")
	fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
	fav_type = models.IntegerField(choices=((1, "视频"), (3, "作者")), default=1, verbose_name=u"收藏类型" )
	add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"用户收藏"
		verbose_name_plural = verbose_name


class UserMessage(models.Model):
	user = models.IntegerField(default=0, verbose_name=u"接收用户")
	message = models.CharField(max_length=500, verbose_name=u"消息内容")
	has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
	add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"用户消息"
		verbose_name_plural = verbose_name


class UserVideo(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name=u"用户")
	video = models.ForeignKey(Video, verbose_name=u"视频")
	add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"用户视频"
		verbose_name_plural = verbose_name


class UserUploadVideo(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name=u"用户")
	video = models.ForeignKey(Video, verbose_name=u"视频")
	add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"用户上传视频"
		verbose_name_plural = verbose_name
