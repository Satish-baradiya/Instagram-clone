from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .forms import UserRegistrationForm, PostUploadForm
from .models import Post
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



def profile(requset, pk):
    user = User.objects.get(id=pk)
    print(user)
    return render(requset, 'insta/userprofile.html',context= {
        'user':user
    })
