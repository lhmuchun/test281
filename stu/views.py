# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.core import serializers

# Create your views here.
from django.views import View


class AreaView(View):
    def get(self, request):
        return render(request, "area.html")


def getInfo(request):
    pid = request.GET.get("pid", -1)
    pid = int(pid)
    areaList = Area.objects.filter(parent_id=pid)
    areaList = serializers.serialize('json',areaList)
    return JsonResponse({'areaList': areaList})