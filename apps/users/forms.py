# -*- coding:utf-8 -*-
from users.models import UserProfile
from django import forms
from captcha.fields import CaptchaField

__author__ = '@Able.Tiger'
__date__ = '2018/3/26 14:27'


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, min_length=6)
	# 此处说明：在前端html中，表单的<input name="username">,<input name="password">
	# 其中,LoginFormz中的字段名字要与之对应


class RegisterForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, min_length=6)
	captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ForgetPasswordForm(forms.Form):
	email = forms.EmailField(required=True)
	captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class PwdResetForm(forms.Form):
	password = forms.CharField(required=True, min_length=6)
	password2 = forms.CharField(required=True, min_length=6)


class ModifyPwdForm(forms.Form):
	password1 = forms.CharField(required=True, min_length=5)
	password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ["image"]


class UploadVideoForm(forms.Form):
	video_name = forms.CharField(required=True)
	video_desc = forms.CharField(required=True)
	video_detail = forms.TextInput()
	video_category = forms.CharField(required=True)
	video_times = forms.CharField(required=True)
	video_image = forms.ImageField(required=True)
	video_video = forms.FileField(required=True)


class UserInfoForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ["nick_name", 'birthday', "gender", "address", "mobile", ]


