#  from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from gd_dp.serializers import (
    UserSerializer,
    GroupSerializer,
    ShopDetail,
    ShopDetailSerializer,
)


class ShopDetailViewSet(viewsets.ModelViewSet):
    queryset = ShopDetail.objects.all()
    serializer_class = ShopDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["origin_shopname", "shopname"]


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
