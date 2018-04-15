# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Author, Post, Tag, Category

class Authoradmin(admin.ModelAdmin):
	list_display=('name','email','created_on')

	search_fields = ['name','email']

	ordering = ['-name']

	list_filter = ['active']

	date_hierarchy = 'created_on'

class Categoryadmin(admin.ModelAdmin):
	list_display=('name','slug','author')

	search_fields=['slug','author']

class Tagadmin(admin.ModelAdmin):
	list_display=('name','slug','author') 

	search_fields=['slug','author']

class Postadmin(admin.ModelAdmin):
	list_display=('tittle','slug','content','author','category')

	search_fields=['slug','author','category','tag']

	ordering = ['-pub_date']

	list_filter = ['pub_date']

	date_hierarchy = 'pub_date'

	#filter_horizontal = ('tag',)

	raw_id_fields = ('tag',)
	#prepopulated_fields = {'slug' : ('tittle',)}

	readonly_fields = ('slug',)

	fields = ('tittle', 'slug', 'content', 'author', 'category', 'tag',)

# Register your models here.

admin.site.register(Author,Authoradmin)
admin.site.register(Post,Postadmin)
admin.site.register(Tag,Tagadmin)
admin.site.register(Category,Categoryadmin)
