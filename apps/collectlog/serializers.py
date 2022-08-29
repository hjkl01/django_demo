from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.collectlog.models import CollectLog


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
        fields = [log.name for log in CollectLog._meta.get_fields()]
