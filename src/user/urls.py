from django.urls import path

from user.views import UserViews, UserListCreateAPIView

app_name = "user"

urlpatterns = [
    path('/all', UserViews.all, name='all'),
    path('/login', UserViews.login, name='login'),
]