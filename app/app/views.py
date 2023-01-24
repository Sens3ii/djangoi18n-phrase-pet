from django.conf import settings
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.utils import translation
from rest_framework import permissions
from rest_framework import viewsets

from app.app.messages import TEST1
from app.app.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def test_view(request):
    message = TEST1
    return JsonResponse({
        'current_user': request.user.username,
        'request_language': request.LANGUAGE_CODE,
        'message': message
    })
