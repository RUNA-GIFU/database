#from django.shortcuts import render

# Create your views here.
# backend/api/inventory/views.py
from rest_framework import viewsets

# from .serializers import MovieSerializer

# class MovieViewSet(viewsets.ModelViewSet):
#     """
#     映画の鑑賞記録を扱うAPIエンドポイント
#     """
#     queryset = Movie.objects.all().order_by('watched_date') # 取得するクエリセットとデフォルトの並び順
#     serializer_class = MovieSerializer # 使用するシリアライザークラスを指定

    # 特定のカスタムロジックが必要な場合、ここにメソッドを追加できます
    # 例: ユーザーごとに映画をフィルタリングする場合
    # def get_queryset(self):
    #     user = self.request.user
    #     return Movie.objects.filter(user=user).order_by('-watched_date')
    
    