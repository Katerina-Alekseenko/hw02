from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUMBER_OF_POSTS: int = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUMBER_OF_POSTS]
    template = 'posts/index.html'
    title_index = 'Это главная страница проекта Yatube'
    context = {'title_index': title_index,
               'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'posts': posts,
        'group': group,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
