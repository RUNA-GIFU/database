# backend/api/movies/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

# --- ここからが変更点 ---
# DefaultRouterのインスタンスを作成
router = DefaultRouter()
# 'movies'というパスの基本名でMovieViewSetをルーターに登録
# これで /api/movies/ や /api/movies/1/ のようなURLが自動生成される
router.register(r'', MovieViewSet, basename='movie')

# urlpatternsでルーターが生成したURLをインクルードする
urlpatterns = [
    path('', include(router.urls)),
]