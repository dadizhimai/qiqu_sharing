# coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from operation.models import UserFavorite


class AddFavView(View):
	"""
	用户添加收藏，取消收藏
	"""
	def post(self, request):
		fav_id = int(request.POST.get('fav_id', 0))
		fav_type = int(request.POST.get('fav_type', 0))
		if not request.user.is_authenticated:
			# 判断用户是否登录，未登录
			return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
		else:
			exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
			if exist_records:
				# 用户收藏已经收藏,则取消收藏
				obj_url = request.META.get('HTTP_REFERER', "/")
				response_data = {}
				response_data['status'] = 'fail'
				response_data['msg'] = '取消收藏'
				response_data['obj_url'] = obj_url
				exist_records.delete()
				return HttpResponse(json.dumps(response_data), content_type='application/json')
				# return HttpResponse('{"status":"fail", "msg":"取消收藏", "obj_url": obj_url }', content_type='application/json')
			else:
				user_fav = UserFavorite()
				if int(fav_id) > 0 and int(fav_type) > 0:
					user_fav.user = request.user
					user_fav.fav_id = int(fav_id)
					user_fav.fav_type = int(fav_type)
					# 添加收藏记录
					user_fav.save()
				else:
					return HttpResponse('{"status":"fail", "msg":"已收藏"}', content_type='application/json')
			return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
