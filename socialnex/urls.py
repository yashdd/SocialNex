from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setting', views.setting, name='setting'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('follower', views.follower, name='follower'),
    path('like_post', views.like_post, name='like_post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    
]
