# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=100,unique=True,verbose_name = "Author Name")
	email = models.EmailField(unique=True)
	active = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
	last_logged_in = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return unicode(self.name+":"+self.email)


class Category(models.Model):
	name = models.CharField(max_length=100,unique=True)
	slug = models.SlugField(max_length=100,unique=True)
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return unicode(self.name)

	def get_absolute_url(self):
		return reverse('post_by_category', args=[self.slug])

	class Meta:
		verbose_name_plural = "Categories"



class Tag(models.Model):
	name = models.CharField(max_length=100,unique=True)
	slug = models.SlugField(max_length=100,unique=True)
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return unicode(self.name)

	def get_absolute_url(self):
		return reverse('post_by_tag', args=[self.slug])


class Post(models.Model):
	tittle = models.CharField(max_length=200)
	slug = models.SlugField(unique=True,help_text="Slug will be generated automatically from the tittle field of post")
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)#field name changed to pub_date again
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag)

	def __unicode__(self):
		return unicode(self.tittle)

	def get_absolute_url(self):
		return reverse('post_detail', args=[self.id])

	def save(self,*args,**kwargs):
		self.slug = slugify(self.tittle)
		super(Post,self).save(*args, **kwargs)


#Class Like(models.Model):
	
	

