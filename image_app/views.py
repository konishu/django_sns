# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostAddForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import cloudinary

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'image_app/index.html', {'posts': posts})


def detail(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    liked = False
    if posts.like.filter(id=request.user.id).exists():
        liked = True
    return render(request, 'image_app/detail.html', {'posts': posts, 'liked': liked})


def like(request):
    posts = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if posts.like.filter(id=request.user.id).exists():
        posts.like.remove(request.user)
        liked = False
    else:
        posts.like.add(request.user)
        liked = True
    return redirect('image_app:detail', post_id=posts.id)


@login_required
def add(request):
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('image_app:index')
    else:
        form = PostAddForm()
    return render(request, 'image_app/add.html', {'form': form})


@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('image_app:detail', post_id=post.id)
    else:
        form = PostAddForm(instance=post)
    return render(request, 'image_app/edit.html', {'form': form, 'post': post})


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('image_app:index')


def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'image_app/signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return redirect('image_app:login')
    return render(request, 'image_app/signup.html')


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('image_app:index')
        else:
            return redirect('image_app:login')
    return render(request, 'image_app/login.html')


def logoutfunc(request):
    logout(request)
    return redirect('image_app:login')


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = user.post_set.all().order_by('-created_at')
    return render(request, 'image_app/user_detail.html', {'user': user, 'posts': posts})


def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('image_app:index')
