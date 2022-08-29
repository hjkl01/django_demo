from rest_framework import serializers

from apps.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "url",
            "website",
            "title",
            "hot_score",
            "img_url",
            "click_count",
            "created_time",
        )
