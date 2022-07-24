from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User


# admin.site.register(UserAdmin)
admin.site.register(User)
admin.site.unregister(Group)