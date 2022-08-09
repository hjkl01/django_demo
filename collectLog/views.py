# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


from collectLog.serializers import UserSerializer, GroupSerializer, CollectLog, CollectLogSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CollectLogViewSet(viewsets.ModelViewSet):
    queryset = CollectLog.objects.all()
    serializer_class = CollectLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id",
        "elapsed",
        "exception",
        "extra",
        "fileinfo",
        "functioN",
        "leveL",
        "line",
        "message",
        "modulE",
        "name",
        "procesS",
        "threaD",
        "insert_time",
        "created_time",
    ]
