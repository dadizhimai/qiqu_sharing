# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from users.models import UserProfile


# Create your models here.
class Video(models.Model):
    author = models.ForeignKey(UserProfile, verbose_name=u"发布作者", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"视频名称")
    desc = models.CharField(max_length=300, verbose_name=u"视频描述")
    detail = models.TextField(verbose_name=u"视频详情")
    degree = models.CharField(max_length=10, choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), verbose_name=u"视频级别")
    learn_times = models.IntegerField(default=0, verbose_name=u"观看时长（分钟）")
    students = models.IntegerField(default=0, verbose_name=u"观看人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"视频展示封面")
    video = models.FileField(upload_to="videos/%Y/%m", verbose_name=u"视频上传", default='')
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(max_length=20, verbose_name=u"视频类别", choices=(("cy", "1"), ("sh", "2"), ("qs", "3")), default=1)
    tag = models.CharField(max_length=10, verbose_name=u"视频标签", default="")
    video_url = models.CharField(max_length=200, verbose_name=u"访问地址", null=True, blank=True)
    video_need = models.CharField(max_length=300, verbose_name=u"视频须知", null=True, blank=True)
    relevant_tell = models.CharField(max_length=300, verbose_name=u"相关推荐", null=True, blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name=u"视频创建时间")

    class Meta:
        verbose_name = "视频基本信息"
        verbose_name_plural = verbose_name

    # def get_learn_users(self):
    #     """
    #     获取学习用户
    #     :return:
    #     """
    #     return self.usercourse_set.all()[:5]

    def __unicode__(self):
        return self.name


class CourseCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"类名称")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "分类名称"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


