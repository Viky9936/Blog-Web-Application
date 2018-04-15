
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Post, Tag, Category

def index(request):
    return HttpResponse("Hello django, I am so much interested to learn about you")

#View function to display the list of posts.
def post_list(request):
    posts = Post.objects.all()
    for post in posts:
        print "....", post.tag.all
    return render(request, 'myapp1/post_list.html',{'posts': posts})

#View fuction to display a single post in detail.

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'myapp1/post_detail.html',{'post': post}) 


#View function to display post by category.

def post_by_category(request,category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    #for post in posts:
        #print "....", post.category__slug.all
    context ={
            'category' : category,
            'posts' : posts
    }
    print category
    return render(request,'myapp1/post_by_category.html',context)

#View to display post by tag.

def post_by_tag(request,tag_slug):
    tag = Tag.objects.get(slug = tag_slug)
    posts = Post.objects.filter(tag__slug=tag_slug)
    context = {
             'tag':tag,
             'posts':posts
    }
    print tag
    return render(request,'myapp1/post_by_tag.html',context)