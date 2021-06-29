from django.contrib.auth.models import User, Group
from rest_framework import serializers

from gd_dp.models import ShopDetail


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDetail
        fields = (
            "id",
            "appname",
            "city",
            "origin_shopname",
            "shopname",
            "district",
            "max_dishes",
            "comments",
            "comment_score",
            "comment_detail",
            "avg_price",
            "shop_cate",
            "address",
            "address_detail",
            "phone",
            "messages",
            "dishes",
            "create_time",
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")
