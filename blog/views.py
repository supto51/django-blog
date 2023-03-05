from django.shortcuts import render, get_object_or_404

from .models import Post


def get_date(post):
    return post['date']


# Create your views here.


def index(request):
    selected_post = Post.objects.all().order_by("-date")[:3]

    return render(request, 'blog/index.html', {
        "posts": selected_post
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/posts.html', {
        "posts": all_posts
    })


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post-details.html', {
        "post": post,
        "post_tags": post.tags.all()
    })
