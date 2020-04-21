# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 22:20
# @Author  : xukang xie
# @FileName: xadmin.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

# 此类可以定义admin后台显示的字段，比如文章列表显示标题，创建时间，
class KeywordAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']
    model_icon = 'fa fa-folder'

from markdown_editor.widgets import XAdminMarkdownWidget
class TagAdmin(object):
    # 展示的字段
    list_display = ['id', 'name', 'slug', 'description']
    # 按描述进行搜索
    search_fields = ['name','description']
    # 筛选
    list_filter = ['id', 'name', 'slug', 'description']
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }
    # 修改图标
    model_icon = 'fa fa-tag'

    # style_fields = {'body':'ueditor'}


class CategoryAdmin(object):
    list_display = ['id','name','description']
    search_fields = ['name']
    list_filter = ['id', 'name', 'slug', 'description']
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }
    model_icon = 'fa fa-plus'

class ArticleAdmin(object):
    list_display = ['id', 'author', 'title','summary','body','img_link','create_date','update_date','views','category','tags','keywords']
    search_fields = ['author', 'title','summary','body','img_link','views','category','tags','keywords']
    list_filter = ['author', 'title','summary','body','img_link','create_date','update_date','views','category','tags','keywords']
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }
    model_icon = 'fa fa-file-text'

# 时间线

class TimelineAdmin(object):
    list_display = ['id', 'side','star_num','icon','icon_color','title','update_date','content']
    search_fields = ['side','star_num','icon','icon_color','title','update_date','content']
    list_filter = ['id', 'side','star_num','icon','icon_color','title','update_date','content']
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }
    model_icon = 'fa fa-calendar'


# 幻灯片
class CarouselAdmin(object):
    list_display = ['id', 'number', 'title', 'content', 'img_url', 'url']
    search_fields = ['number', 'title', 'content', 'img_url']
    list_filter = ['number', 'title', 'content', 'img_url']
    model_icon = 'fa fa-picture-o'


# 链接标签
class SilianAdmin(object):
    list_display = ['id', 'badurl', 'remark', 'add_date']
    search_fields = ['badurl', 'remark']
    list_filter = ['badurl', 'remark']
    model_icon = 'fa fa-book'


# 友情分类
class FriendLinkAdmin(object):
    list_display = ['id', 'name', 'description', 'is_active', 'is_show']
    search_fields = ['name', 'description', 'is_active', 'is_show']
    list_filter = ['name', 'description', 'is_active', 'is_show']
    model_icon = 'fa fa-link'


# 关于博客
class AboutBlogAdmin(object):
    list_display = ['id', 'body', 'create_date']
    search_fields = ['body', 'create_date']
    list_filter = ['body', 'create_date']
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }







xadmin.site.register(Keyword,KeywordAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Timeline,TimelineAdmin)


xadmin.site.register(Carousel,CarouselAdmin)
xadmin.site.register(Silian,SilianAdmin)
xadmin.site.register(FriendLink,FriendLinkAdmin)

xadmin.site.register(AboutBlog,AboutBlogAdmin)

# 修改xadmin的基础配置
class BaseSetting(object):
    # 允许使用主题
    enable_themes = True
    use_bootswatch = True


# 修改xadmin的全局配置
class GlobalSetting(object):
    site_title = '博客后台管理'
    site_footer = 'Copyright © 2020 Kevin. Powered by Django,Xadmin.'

    # Models收起功能
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting )