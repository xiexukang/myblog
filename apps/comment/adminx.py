# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 20:04
# @Author  : xukang xie
# @FileName: adminx.py
# @Software: PyCharm

import xadmin
from .models import *

class CommentAdmin(object):
    list_display = ['id', 'author', 'content', 'parent', 'rep_to']
    search_fields = ['author']
    list_filter = ['id', 'author', 'content', 'parent', 'rep_to']
    model_icon = "fa fa-commenting-o"

class ArticleCommentAdmin(object):
    list_display = ['id', 'belong']
    search_fields = ['belong']
    list_filter = ['id', 'belong']
    model_icon = "fa fa-commenting-o"

class NotificationAdmin(object):
    list_display = ['id', 'create_p', 'get_p', 'comment', 'is_read', 'create_date']
    search_fields = ['create_p', 'get_p', 'comment', 'is_read']
    list_filter = ['id', 'create_p', 'get_p', 'comment', 'is_read']
    model_icon = "fa fa-bell-o"

xadmin.site.register(Notification,NotificationAdmin)
xadmin.site.register(ArticleComment,ArticleCommentAdmin)