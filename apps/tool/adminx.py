# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 20:42
# @Author  : xukang xie
# @FileName: adminx.py
# @Software: PyCharm
import xadmin
from .models import *

class ToolCategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']
    model_icon = "fa fa-wrench"


class ToolLinkAdmin(object):
    list_display = ['id', 'name', 'description', 'link', 'category']
    search_fields = ['name', 'description', 'link', 'category']
    list_filter = ['id', 'name', 'description', 'link', 'category']


xadmin.site.register(ToolCategory, ToolCategoryAdmin)
xadmin.site.register(ToolLink, ToolLinkAdmin)