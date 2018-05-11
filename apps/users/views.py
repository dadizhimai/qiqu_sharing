# -*- coding:utf-8 -*-
import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from requests import get

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetPasswordForm, ModifyPwdForm, UploadImageForm, UserInfoForm, ForgetPasswordForm, PwdResetForm, UploadVideoForm
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequireMixin
from operation.models import UserVideo, UserFavorite, UserMessage, UserUploadVideo
from .models import Banner
from video.models import Video
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


class Index(View):
	"""
	首页
	"""

	def get(self, request):
		current_nav = ''
		all_banners = Banner.objects.all().order_by("index")
		banner_chuyi_lists = Video.objects.filter(category='cy').order_by('-add_time')[:2]
		banner_shenghuo_lists = Video.objects.filter(category='sh').order_by('add_time')[:2]
		banner_liyi_lists = Video.objects.filter(category='qs').order_by('add_time')[:2]

		chuyi_lists = Video.objects.filter(category='cy').order_by('-add_time')[2:8]
		shenghuo_lists = Video.objects.filter(category='sh').order_by('add_time')[:6]
		liyi_lists = Video.objects.filter(category='qs').order_by('add_time')[:6]
		return render(request, 'index.html', locals())


class CustomBackends(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			user = get(Q(username=username) | Q(email=username))  # 使用get只能返回一个，相当于一个验证
			if user.check_password(password):
				return user
		except Exception as e:
			return None


# 激活验证
class ActiveUserView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code=active_code)
		if all_records:
			for record in all_records:
				email = record.email  # 取出邮箱激活验证码一样的邮箱
				user = get(email=email)
				user.is_active = True  # 修改激活字段为True
				user.save()
		else:
			return render(request, 'active_fail.html')
		return render(request, 'login.html')


# 注册
class RegisterView(View):

	def get(self, request):
		register_form = RegisterForm()
		return render(request, 'register.html', {'register_form': register_form})

	def post(self, request):
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			email = request.POST.get('email', '')
			if UserProfile.objects.filter(email=email):
				return render(request, 'register.html', {'register_form': register_form, 'message': u'用户已经存在'})
			password = request.POST.get('password', '')
			# 保存用户数据表
			user = UserProfile()
			user.email = email
			user.username = email
			user.password = make_password(password)
			user.is_active = False
			user.save()
			# 发送邮箱验证激活
			send_register_email(email, 'register')
			return render(request, 'index.html', locals())
		else:
			return render(request, 'register.html', {'register_form': register_form})


# 登录
class LoginView(View):
	"""
	用户登录post请求，处理逻辑
	"""

	def get(self, request):
		return render(request, 'login.html', locals())

	def post(self, request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():  # 验证form,是否合法
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			user = authenticate(username=username, password=password)  # 验证登录名和密码
			if user is not None:
				if user.is_active:  # 验证是否激活
					login(request, user)
					return render(request, 'index.html', locals())
				else:
					return render(request, 'login.html', {'message': '用户未激活！'})
			else:
				return render(request, 'login.html', {'message': '用户名或密码错误！'})
		else:
			return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):
	"""
	用户登出
	"""

	def get(self, request):
		logout(request)
		from django.core.urlresolvers import reverse
		return HttpResponseRedirect(reverse('index'))


# 找回秘密
class ForgetPasswordView(View):
	def get(self, request):
		forget_pwd_form = ForgetPasswordForm()
		return render(request, 'forgetpwd.html', locals())

	def post(self, request):
		forget_pwd_form = ForgetPasswordForm(request.POST)
		if forget_pwd_form.is_valid():
			email = request.POST.get('email', '')
			# 找回密码发送邮件认证
			send_register_email(email, 'forget')
			return render(request, 'send_success.html')
		else:
			meg = u'用户名错误,请重新输入！'
			{'message': meg}
			return render(request, 'forgetpwd.html', locals())


# 重置密码
class PwdResetView(View):
	def get(self, request, reset_code):
		all_records = EmailVerifyRecord.objects.filter(code=reset_code)
		if all_records:
			for record in all_records:
				email = record.email  #
				return render(request, 'password_reset.html', locals())
		else:
			return render(request, 'active_fail.html')


class ModifyPwdView(View):
	def post(self, request):
		reset_pwd_form = PwdResetForm(request.POST)
		if reset_pwd_form.is_valid():
			password = request.POST.get('password', '')
			password2 = request.POST.get('password2', '')
			email = request.POST.get('email', '')
			if password == password2:
				user = UserProfile.objects.get(email=email)
				user.password = make_password(password)
				user.save()
				return render(request, 'login.html')
			else:
				{'meg': u'两次密码不一样'}
				return render(request, 'password_reset.html', locals())
		else:
			email = request.POST.get('email', '')
			return render(request, 'password_reset.html', locals())


# 个人中心
class UserInfoView(LoginRequireMixin, View):
	"""
	用户个人信息
	"""

	def get(self, request):
		current_nav = 'user-info'
		return render(request, "usercenter-info.html", locals())

	def post(self, request):
		user_info_form = UserInfoForm(request.POST, instance=request.user)
		"""
		instance:这是个关键参数
		这里是使用了model form，所以需要instance参数，来指明用了哪个实例（哪条数据）来修改
		"""
		if user_info_form.is_valid():
			user_info_form.save()
			return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")
		else:
			return HttpResponse(json.dumps(user_info_form.errors), content_type="application/json")

	"""
	json.dump(user_info_form.errors):获取了cleaned_data的错误信息
	"""


class UploadImageView(LoginRequireMixin, View):
	"""
	用户修改头像
	"""

	def post(self, request):
		image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
		if image_form.is_valid():
			request.user.save()
			return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")
		else:
			return HttpResponse('{"status": "fail", "msg":"修改失败"}', content_type="application/json")


class UpdatePwdView(View):
	"""
	个人中心密码修改
	"""

	def post(self, request):
		modify_form = ModifyPwdForm(request.POST)
		if modify_form.is_valid():
			pwd1 = request.POST.get("password1", "")
			pwd2 = request.POST.get("password2", "")
			if pwd1 != pwd2:
				return HttpResponse('{"status": "fail", "msg":"修改失败"}', content_type="application/json")
			user = request.user
			user.password = make_password(pwd2)
			user.save()
			return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")
		else:
			return HttpResponse(json.dump(modify_form.errors), content_type="application/json")


# 发送邮箱验证码
class SendEamilCodeView(LoginRequireMixin, View):
	"""
	发送邮箱验证码
	"""

	def get(self, request):
		email = request.GET.get("email", "")
		if UserProfile.objects.filter(email=email):
			return HttpResponse('{"email": "邮箱已存在"}', content_type="application/json")
		send_register_email(email, "update_email")
		return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")


# 修改个人邮箱
class UpdateEmailView(LoginRequireMixin, View):
	"""
		修改个人邮箱
		"""

	def post(self, request):
		email = request.POST.get("email", "")
		code = request.POST.get("code", "")

		existed_codes = EmailVerifyRecord.objects.filter(email=email, code=code, send_type="update_email")
		if existed_codes:
			user = request.user
			user.email = email
			user.save()
			return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")
		else:
			return HttpResponse('{"email": "验证码出错"}', content_type="application/json")


class MyCourseView(LoginRequireMixin, View):
	"""
	我的课程
	"""

	def get(self, request):
		current_nav = 'user-video'
		user_videos = UserVideo.objects.filter(user=request.user)
		# 课程列表分页
		try:
			page = request.GET.get('page', '1')
		except PageNotAnInteger:
			page = 1
		p = Paginator(user_videos, 3, request=request)
		user_videos = p.page(page)
		return render(request, "usercenter-mycourse.html", locals())


class MyUploadVideoView(LoginRequireMixin, View):
	"""
	我的上传
	"""

	def get(self, request):
		current_nav = 'user-up-video'
		user_videos = UserUploadVideo.objects.filter(user=request.user)
		# 课程列表分页
		try:
			page = request.GET.get('page', '1')
		except PageNotAnInteger:
			page = 1
		p = Paginator(user_videos, 9, request=request)
		user_videos = p.page(page)
		return render(request, "usercenter-upload-video.html", locals())


class MyUploadView(LoginRequireMixin, View):
	"""
	视频上传
	"""

	def get(self, request):
		current_nav = 'user-up'
		return render(request, 'usercenter-upload.html', locals())


class MyUploadVideoView(LoginRequireMixin, View):
	"""
	视频上传
	"""

	def post(self, request):
		video_image = request.FILES['video_image']
		video_video = request.FILES['video_video']
		video_name = request.POST.get('video_name',)
		video_desc = request.POST.get('video_desc',)
		video_detail = request.POST.get('video_detail',)
		video_category = request.POST.get('video_category',)
		video_times = request.POST.get('video_times',)

		video_form = UploadVideoForm(request.POST, request.FILES)
		# if video_form.is_valid():
		# 	video_name = video_form.video_name
		# 	video_desc = video_form.video_desc
		# 	video_detail = video_form.video_detail
		# 	video_category = video_form.video_degree
		# 	video_times = video_form.video_times
		# 	video_image = request.FILES['video_image']
		# 	video_video = request.FILES['video_video']

		video = Video()
		video.name = video_name
		video.desc = video_desc
		video.detail = video_detail
		video.category = video_category
		video.learn_times = video_times
		video.image = video_image
		video.video = video_video
		video.save()

		return HttpResponse('{"status": "success", "msg":"上传成功"}', content_type="application/json")
		# else:
		# 	return HttpResponse('{"status": "fail", "msg":"上传失败"}', content_type="application/json")


######
class MyFavAuthorView(LoginRequireMixin, View):
	"""
	我收藏的授课讲师
	"""

	def get(self, request):
		teacher_list = []
		fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
		for fav_teacher in fav_teachers:
			teacher_id = fav_teacher.id
			teacher = get(id=teacher_id)
			teacher_list.append(teacher)
		try:
			page = request.GET.get('page', '1')
		except PageNotAnInteger:
			page = 1
		p = Paginator(teacher_list, 8, request=request)
		teacher_list = p.page(page)
		return render(request, "usercenter-fav-author.html", locals())


class MyFavCourseView(LoginRequireMixin, View):
	"""
	我收藏的视频
	"""

	def get(self, request):
		current_nav = 'user-course'
		course_list = []
		fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
		for fav_course in fav_courses:
			course_id = fav_course.id
			course = Video.objects.get(id=course_id)
			course_list.append(course)
		try:
			page = request.GET.get('page', '1')
		except PageNotAnInteger:
			page = 1
		p = Paginator(course_list, 8, request=request)
		course_list = p.page(page)
		return render(request, "usercenter-fav-course.html", locals())


class MyMessageView(LoginRequireMixin, View):
	"""
	我的消息
	"""

	def get(self, request):
		current_nav = 'user-news'
		all_messages = UserMessage.objects.filter(user=request.user.id)

		all_unread_message = UserMessage.objects.filter(user=request.user.id, has_read=False)
		for unread_message in all_unread_message:
			unread_message.has_read = True
			unread_message.save()

		return render(request, "usercenter-message.html", locals())


def page_no_found(request):
	"""
	全局404
	:param request:
	:return:
	"""
	from django.shortcuts import render_to_response
	response = render_to_response("404.html", {})
	response.status_code = 404
	return response


def page_error(request):
	"""
	全局500
	:param request:
	:return:
	"""
	from django.shortcuts import render_to_response
	response = render_to_response("500.html", {})
	response.status_code = 500
	return response
