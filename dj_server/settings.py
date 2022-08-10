"""
Django settings for dj_server project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path
import environ


env = environ.Env()
env.read_env(".env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-rq6b^cgpjjho@@jf$&2^-30%c7_zp&pxc(byd-^%oo(56fcz2@",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=True)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "import_export",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    # "gd_dp",
    "collectLog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dj_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dj_server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}
#  print(DATABASES)
#  DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#      }
#  }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAdminUser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        #  "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60 * 1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

#  STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# simpleui
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# 首页
#  SIMPLEUI_HOME_PAGE = "/"
# 首页标题
SIMPLEUI_HOME_TITLE = "数据平台"

# 首页显示服务器、python、django、simpleui相关信息
SIMPLEUI_HOME_INFO = True

# 首页显示快速操作
SIMPLEUI_HOME_QUICK = True

# 首页显示最近动作
SIMPLEUI_HOME_ACTION = True

# 登录页粒子动画，默认开启，False关闭
# SIMPLEUI_LOGIN_PARTICLES = False

# 让simpleui 不要收集相关信息
SIMPLEUI_ANALYSIS = True

# 指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目
# 不填该项或者为False的时候，默认从第三方的cdn获取
#  SIMPLEUI_STATIC_OFFLINE = False
SIMPLEUI_STATIC_OFFLINE = True

# 隐藏所有simpleui和simplepro相关的信息
SIMPLEPRO_INFO = True

# 配置Simple Pro是否显示首页的图标，默认为True，显示图表，False不显示
SIMPLEPRO_CHART_DISPLAY = False


# 自定义simpleui 菜单
SIMPLEUI_CONFIG = {
    # 在自定义菜单的基础上保留系统模块
    "system_keep": True,
    "dynamic": False,
    "menus": [
        {"name": "SWAGGER", "url": "/swagger/", "icon": "fa fa-user"},
        {
            "name": "WORK",
            "icon": "fa fa-server",
            "models": [
                {"name": "GITEA", "url": "https://nj.hjkl01.cn:33000/", "icon": "fa fa-code"},
                {"name": "CLOUDREVE", "url": "https://nj.hjkl01.cn:15212/", "icon": "fa fa-cloud"},
                {"name": "ALIST", "url": "https://nj.hjkl01.cn:15244/", "icon": "fa fa-file"},
                {"name": "FRPS", "url": "https://nj.hjkl01.cn:17400/", "icon": "fa fa-wifi"},
            ],
        },
        {
            "name": "PLAY",
            "icon": "fa fa-video",
            "models": [
                {"name": "ARIA2", "url": "http://nj.hjkl01.cn:16880/", "icon": "fa fa-download"},
                {"name": "MOVIE", "url": "https://nj.hjkl01.cn:18096/", "icon": "fa fa-film"},
                {"name": "MUSIC", "url": "https://nj.hjkl01.cn:13000/", "icon": "fa fa-music"},
            ],
        },
        {
            "name": "Myself",
            "icon": "fa fa-blog",
            "models": [
                {"name": "BLOG", "url": "https://pages.hjkl01.cn/"},
                # {"name": "GAYHUB", "url": "https://github.com/", "newTab": True, "icon": "fab fa-github"},
                {"name": "抽屉", "url": "https://dig.chouti.com/"},
                # {"name": "V2EX", "url": "https://www.v2ex.com/"},
                {"name": "ROUTER", "url": "https://www.right.com.cn/forum/"},
                # {"name": "TELEGRAM", "url": "https://web.telegram.org/z/"},
                # {"name": "TWITTER", "url": "https://twitter.com/explore"},
            ],
        },
    ],
}

# 是否显示默认图标，默认=True
# SIMPLEUI_DEFAULT_ICON = True
SIMPLEUI_DEFAULT_ICON = False
