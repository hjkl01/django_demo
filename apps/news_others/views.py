from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.decorators import action

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from apps.news_others.serializers import NewsOthers, NewsOthersSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)


class NewsOthersViewSet(viewsets.ModelViewSet):
    queryset = NewsOthers.objects.all()
    serializer_class = NewsOthersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "url",
        "website",
        "title",
        "filename",
        "if_sended",
        "created_time",
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(
        methods=["POST"],
        detail=False,
        url_path="sended",
        permission_classes=[permissions.IsAuthenticated],
    )
    def getSended(self, request, *args, **kwargs):
        news = NewsOthers.objects.filter(if_sended=0)
        serializer = NewsOthersSerializer(news, many=True)
        return JSONResponse(serializer.data)

    @action(
        methods=["POST"],
        detail=False,
        url_path="update",
        permission_classes=[permissions.IsAuthenticated],
    )
    def updateSended(self, request, *args, **kwargs):
        ids = request._data["ids"]
        print(ids)

        NewsOthers.objects.filter(id__in=ids).update(if_sended=1)
        return JSONResponse(ids)
