from django.urls import path
from .import views
from django.contrib.auth import views as authviews
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',authviews.LoginView.as_view(template_name='insta/login.html'),name='login'),
    path('logout',authviews.LogoutView.as_view(template_name='insta/logout.html'),name='logout'),
    path('post',views.post,name='post')
]
