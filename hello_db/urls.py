# api/hello_db/urls.py

from django.urls import path
from . import views  # views.py にエンドポイントがあれば

urlpatterns = [
    # 例：path('', views.index, name='index'),
    path('backend/', views.Db.as_view()),
]
