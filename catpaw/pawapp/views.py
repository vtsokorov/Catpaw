from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()

    return render(
        request,
        'pawapp/post/list.html', {
            'posts': posts
        }
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    # post = get_object_or_404(
    #     Post, id=id, status=Post.Status.PUBLISHED
    # )
    # try:
    #     post = Post.publish.get(id=id)
    # except:
    #     raise Http404('Not found post')

    return render(
        request,
        'pawapp/post/detail.html', {
            'post': post
        }
    )