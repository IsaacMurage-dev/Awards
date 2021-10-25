from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Rating
from .forms import ProfileForm, NewPostForm, ProjectRatingForm
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def profile(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if new_profile.is_valid():
            new_profile.save()
            print(new_profile.fields)
            # print(new_profile.fields.profile_picture)
            return redirect('profile')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', locals())


@login_required(login_url='/accounts/login/')
def project(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'projects.html', locals())


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('project')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def user(request, user_id):
    user_object = get_object_or_404(User, pk=user_id)
    if request.user == user_object:
        return redirect('profile')
    user_projects = user_object.posts.all()
    return render(request, 'user.html', locals())


def single_project(request, c_id):
    current_user = request.user
    current_project = Post.objects.get(id=c_id)
    ratings = Rating.objects.filter(post_id=c_id)
    usability = Rating.objects.filter(post_id=c_id).aggregate(Avg('usability_rating'))
    content = Rating.objects.filter(post_id=c_id).aggregate(Avg('content_rating'))
    design = Rating.objects.filter(post_id=c_id).aggregate(Avg('design_rating'))

    return render(request, 'project.html',
                  {"project": current_project, "user": current_user, 'ratings': ratings, "design": design,
                   "content": content, "usability": usability})


def review_rating(request, id):
    current_user = request.user

    current_project = Post.objects.get(id=id)

    if request.method == 'POST':
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = current_project
            rating.user = current_user
            rating.save()
            return redirect('project', id)
    else:
        form = ProjectRatingForm()

    return render(request, 'rating.html', {'form': form, "project": current_project, "user": current_user})
