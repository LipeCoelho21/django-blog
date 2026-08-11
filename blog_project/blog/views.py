from django.http import Http404
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag
# Create your views here.

# View function: Display the starting/home page with all posts
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3] # Order posts by date in descending order and get the latest 3
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })

# View function: Display the posts page (same as starting_page)
def all_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {
        "all_posts": posts
    })

# View function: Display a single post detail page
def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
