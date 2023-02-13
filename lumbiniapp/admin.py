from django.contrib import admin
from . models import *

# Register your models here.

from . models import AppSetting, AboutUs, FactFigure, MessageForm, ChooseUs, Collaboration, Gallery, Slider, Courses, News, FAQCategories, FAQ, SocialLinks,UseFullLink, Feedback


class ColAppsetting(admin.ModelAdmin):
    list_display = ( 'name', 'logo', 'phone', 'email')
    list_filter = ('name', 'logo', 'phone', 'email')
    search_fields = ('name', 'phone')

class ColAboutUS(admin.ModelAdmin):
    list_display = ('name','title', 'discription')
    list_filter = ('name','title', 'discription')

class ColFactFigure(admin.ModelAdmin):
    list_display = ('name','total_students','total_courses', 'total_project', 'total_teacher')
    list_filter = ('name','total_students','total_courses')

class ColMessageFOrm(admin.ModelAdmin):
    list_display = ('name', 'position', 'image')

class COlChooseUs(admin.ModelAdmin):
    list_display= ('name','title', 'icon_class','is_active')

class COlCOllaboration(admin.ModelAdmin):
    list_display= ('id', 'name', 'image', 'link')
    search_field = ('id')


class COlGallery(admin.ModelAdmin):
    list_display=('id','name', 'image')

class ColSlider(admin.ModelAdmin):
    list_display=('title', 'image', 'button_text')

class ColCourses(admin.ModelAdmin):
    list_display=('id', 'title', 'image', 'display_order', 'is_active')
    search_fields=('display_order', 'is_active')

class ColNews(admin.ModelAdmin):
    list_display=('id', 'title', 'image', 'views', 'is_active')
    search_fields=('views', 'is_active')

class ColFAQCategories(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'display_order')
    search_fields = ('id', 'name')

class COlFAQ(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'catagory')
    search_fields = ('id', 'catagory')


class ColSocialLinks(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'link', 'is_activate')

class ColUseFullLinks(admin.ModelAdmin):
    list_display = ('id','name', 'icon_class', 'link', 'is_activate')

class ColFeedback(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone_number', 'subject', 'feedback')
    search_fields = ('id', 'phone_number')










admin.site.register(AppSetting,ColAppsetting)
admin.site.register( AboutUs, ColAboutUS)
admin.site.register(FactFigure, ColFactFigure)
admin.site.register(MessageForm, ColMessageFOrm )
admin.site.register(ChooseUs, COlChooseUs)
admin.site.register(Collaboration, COlCOllaboration)
admin.site.register(Gallery,COlGallery)
admin.site.register(Slider,ColSlider)
admin.site.register(Courses, ColCourses)
admin.site.register(News,ColNews)
admin.site.register(FAQCategories,ColFAQCategories)
admin.site.register(FAQ,COlFAQ)
admin.site.register(SocialLinks,ColSocialLinks)
admin.site.register(UseFullLink , ColUseFullLinks)
admin.site.register(Feedback, ColFeedback)
