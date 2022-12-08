from django.urls import path

from user.views import UserViews

app_name = "user"

urlpatterns = [
    path('/all', UserViews.all, name='all'),

]