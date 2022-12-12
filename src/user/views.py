from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from user.filters import UserFilterSet
from user.models import User
from user.serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    throttle_scope = "datalist"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilterSet


class UserViews():
    @api_view(['GET'])
    def all(request):
        user_list = []

        user_objects = User.objects.values()
        if user_objects:
            for user_object in user_objects:
                user_list.append(user_object)
        return Response(user_list)

    @api_view(['POST'])
    def login(request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_list = []

        return Response(user_list)