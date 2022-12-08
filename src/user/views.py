from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User


class UserViews():
    @api_view(['GET'])
    def all(request):
        user_list = []

        user_objects = User.objects.values()
        if user_objects:
            for user_object in user_objects:
                user_list.append(user_object)
        return Response(user_list)