# coding:utf-8
from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEamilCodeView, UpdateEmailView
from .views import MyCourseView, MyFavAuthorView, MyMessageView, MyFavCourseView, MyUploadVideoView, MyUploadView,MyUploadVideoView

__Author__ = 'eyu Fanne'
__Date__ = '2017/7/27'


urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEamilCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    # 我的上传列表
    url(r'^myuploadvideo/$', MyUploadVideoView.as_view(), name="myuploadvideo"),

    # 上传视频
    url(r'^myupload/$', MyUploadView.as_view(), name="myupload"),
    url(r'^myupload/vidoe/$', MyUploadVideoView.as_view(), name="myvideo"),

    # 我收藏的课程机构
    # url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

    # 我收藏的讲师
    url(r'^myfav/author/$', MyFavAuthorView.as_view(), name="myfav_author"),

    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage"),
]