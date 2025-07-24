# backend/api/movies/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-watched_date')
    serializer_class = MovieSerializer

    
    def create(self, request, *args, **kwargs):
        # --- ここに探偵を仕掛けます！ ---
        print("探偵より報告：createメソッドが呼び出されました。")
        print("受け取ったデータ:", request.data)
        # --------------------------------

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)