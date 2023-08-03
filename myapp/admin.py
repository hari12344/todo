from django.contrib import admin
from .models.userInfo import UserInfo
from .models.todo import TODO

# Register your models here.
# class UserInfoAdmin(admin.ModelAdmin):

admin.site.register(UserInfo)
admin.site.register(TODO)