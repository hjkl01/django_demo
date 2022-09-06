import random
from datetime import datetime, timedelta

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.decorators import action

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from apps.news.serializers import News, NewsSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "url",
        "website",
        "title",
        "if_sended",
        "hot_score",
        "click_count",
        "created_time",
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(
        methods=["POST"],
        detail=False,
        url_path="reload",
        permission_classes=[permissions.AllowAny],
    )
    def getReload(self, request, *args, **kwargs):
        print("args--> ", args)
        print("kwargs--> ", kwargs)
        yestoday = datetime.today() - timedelta(days=1)
        news_ids = [
            n.id for n in News.objects.filter(created_time__gte=yestoday.date())
        ]
        ids = random.choices(news_ids, k=15)
        print(ids)

        news = News.objects.filter(id__in=ids)
        serializer = NewsSerializer(news, many=True)
        return JSONResponse(serializer.data)

    @action(
        methods=["POST"],
        detail=False,
        url_path="sended",
        permission_classes=[permissions.IsAuthenticated],
    )
    def getSended(self, request, *args, **kwargs):
        news = News.objects.filter(if_sended=0)
        serializer = NewsSerializer(news, many=True)
        return JSONResponse(serializer.data)

    @action(
        methods=["POST"],
        detail=False,
        url_path="update",
        permission_classes=[permissions.IsAuthenticated],
    )
    def updateSended(self, request, *args, **kwargs):
        print("request--> ", request.data)
        ids = request.data.get("ids")
        print(ids)
        # ids = json.loads(ids)

        News.objects.filter(id__in=ids).update(if_sended=1)
        return JSONResponse(ids)
