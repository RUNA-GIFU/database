# # backend/config/settings/development.py (変更不要)

# import os
# from .base import *

# # DEBUG 設定を環境変数から取得するように変更
# # docker-compose.yml の DJANGO_DEBUG 環境変数に対応
# # DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
# DEBUG = True

# # ALLOWED_HOSTS も設定 (Djangoがアクセスを許可するホスト名)
# # Dockerコンテナからのアクセスを許可するために 'backend' を追加
# # 開発中は'*'で全て許可することもありますが、セキュリティ的には非推奨
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'backend', '0.0.0.0']

# # DATABASES のセクションを探してください。
# # もしSQLite (django.db.backends.sqlite3) の設定があれば、以下のようにMySQL用に完全に置き換えます。
# # base.py に DATABASES がある場合は、ここで上書きするか、base.py を直接修正します。
# # 経験上、development.py でローカルDB設定を上書きすることが多いです。
# DATABASES = {
#   'default' : {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME' : 'app',
#     'USER' : 'root',
#     'PASSWORD' : 'password',
#     'HOST' : 'host.docker.internal',
#     'PORT' : '53306',
#     'ATOMIC_REQUESTS' : True
#   }
# }
# # config/settings.py

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'api.hello_db',
#     'api.inventory',
#     'api.movies',
#     'corsheaders',
# ]

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',  # ← 最初の方に追加
#     'django.middleware.common.CommonMiddleware',
# ]

# CORS_ALLOW_ALL_ORIGINS = True

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR.parent.parent / 'media'


import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'backend', '0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host.docker.internal',
        'PORT': '53306',
        'ATOMIC_REQUESTS': True,
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api.hello_db',
    'api.inventory',
    'api.movies',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',         
    'corsheaders.middleware.CorsMiddleware',                        
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',      
    'django.contrib.messages.middleware.MessageMiddleware',         
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://127.0.0.1:8000",  # ← 実際の Codespace URL に変更可
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent.parent / 'media'
