#  from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from gd_dp.serializers import (
    ShopDetail,
    ShopDetailSerializer,
)


class ShopDetailViewSet(viewsets.ModelViewSet):
    queryset = ShopDetail.objects.all()
    serializer_class = ShopDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["origin_shopname", "shopname"]
