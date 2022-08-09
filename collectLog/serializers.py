from django.contrib.auth.models import User, Group
from rest_framework import serializers

from collectLog.models import CollectLog


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")


class CollectLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectLog
        fields = (
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
        )
