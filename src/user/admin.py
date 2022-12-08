from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')


admin.site.register(User, UserAdmin)