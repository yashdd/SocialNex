from django.contrib import admin
from .models import Like_Post, Profile,Post,Followers_count
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like_Post)
admin.site.register(Followers_count)