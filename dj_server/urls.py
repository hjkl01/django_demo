"""dj_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.views import static
from django.conf import settings

from tyadmin_api.views import AdminIndexView


urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^$", RedirectView.as_view(url="/xadmin/")),
    re_path("^xadmin/.*", AdminIndexView.as_view()),
    path("api/xadmin/v1/", include("tyadmin_api.urls")),
    url(r"^static/(?P<path>.*)$", static.serve, {"document_root": settings.STATIC_ROOT}, name="static"),
]
