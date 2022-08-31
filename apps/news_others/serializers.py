from rest_framework import serializers

from apps.news_others.models import NewsOthers


class NewsOthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsOthers
        fields = (
            "id",
            "url",
            "website",
            "title",
            "filename",
            "created_time",
        )
