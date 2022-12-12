from django.contrib import admin
from django.urls import path, include

from user.views import UserViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', include('user.urls', namespace="user")),
    path('', UserViews.all),
]
