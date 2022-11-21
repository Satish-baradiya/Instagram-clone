from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .forms import UserRegistrationForm, PostUploadForm
from .models import Post, UserFollowing
from django.contrib.auth.models import User

# Create your views here.



def home(request):
    user = request.user
    if user:
        posts = Post.objects.filter(user=user.id)

    return render(request,'insta/home.html',context={
        'posts':posts
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'insta/register.html', context)


def post(request):
    user = request.user
    if request.method == 'POST':
        form = PostUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('img')
            description = form.cleaned_data.get('description')

            newpost = Post.objects.create(user=user,img=image,description=description)
            newpost.save()
            return redirect('home')
    else:
        form = PostUploadForm()
    return render(request,'insta/post.html',context={'form':form})  


def user_listing(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request,'insta/userlist.html',context={
        'users':users
    })


def profile(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        current_user = request.user
        userfollowing = UserFollowing.objects.get(user_id=current_user.id)
        data = request.POST
        if "follow" in data:
            userfollowing.following_user_id.add(user)
        elif "unfollow" in data:
            userfollowing.following_user_id.remove(user)

    return render(request, 'insta/userprofile.html',context= {
        'user':user
    })


def post_list(request):
    user = request.user
    print('Current user is ',user.username)
    followers = UserFollowing.objects.filter(user_id=user.id).values_list('following_user_id',flat=True)
    print('current user is follows ', followers)
    posts = Post.objects.filter(user__id__in=followers)
    print(posts)

    return render(request, 'insta/postlist.html',context={
        'posts':posts
    })
