# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
	nick_name = models.CharField\
		(max_length=50, verbose_name=u"昵称", default="")
	birthday = models.DateField\
		(verbose_name=u"生日", null=True, blank=True)
	gender = models.CharField\
		(max_length=10, choices=
		(("male", u"男"), ("female", u"女")), default='female')
	address = models.CharField(max_length=100, default=u"")
	mobile = models.CharField(max_length=11, null=True, blank=True)
	image = models.ImageField\
		(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

	class Meta:
		verbose_name = u"用户信息"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.username


class EmailVerifyRecord(models.Model):
	code = models.CharField(max_length=20, verbose_name=u"验证码")
	email = models.EmailField(max_length=50, verbose_name=u"邮箱")
	send_type = models.CharField(verbose_name=u"验证码类型", max_length=10, choices=(("register", u"注册"), ("forget", u"找回密码")))
	send_time = models.DateField(verbose_name=u"发送时间", default=datetime.now)

	class Meta:
		verbose_name = u"邮箱验证码"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return '{0}({1})'.format(self.code, self.email)


class PostBar(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name=U"贴吧发言人")
	contents = models.TextField(verbose_name=u"发言内容")
	pid = models.IntegerField(verbose_name=u"父id")
	cid = models.IntegerField(verbose_name=u"子id")
	add_time = models.DateField(default=datetime.now, verbose_name=u"发布时间")

	class Meta:
		verbose_name = u"贴吧留言"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.contents


class Banner(models.Model):
	title = models.CharField(max_length=100, verbose_name=u"标题")
	image = models.ImageField(max_length=100, upload_to="banner/%Y%m", verbose_name=u"轮播图")
	url = models.URLField(max_length=200, verbose_name=u"访问地址")
	index = models.IntegerField(default=100, verbose_name=u"顺序")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"轮播图"
		verbose_name_plural = verbose_name