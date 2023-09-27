# 共通設定読込
from .base import *

# prod環境設定ファイル

SECRET_KEY = "django-insecure-*wb*vqt7bg8wizzkay2&a1yxwci8t!b8_tw2_)dqqf5uj3dq^b"

# SECURITY WARNING: don't run with debug turned on in production!
# ただし、404エラーなどの共通画面を出すのにFalseにしないといけなくそうすると
# 静的ファイルが読まれないので、
# ・DEBUG = False
# ・ALLOWED_HOSTS = ["127.0.0.1"]
# ・runserver --insecure で起動する
DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# DB接続文字列要変更
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "projectdb",
        "USER": "root",
        "PASSWORD": "admin",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

# ログ出力設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    # フォーマット設定
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s | %(thread)d %(message)s"
        },
    },
    # ハンドラ設定
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "filename": "/var/logs/app.log",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        # 追加
        "kintai": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    }
}
