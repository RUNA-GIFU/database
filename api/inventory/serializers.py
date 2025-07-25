# backend/api/inventory/serializers.py
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' # Movieモデルの全てのフィールドを対象とする
        # 必要に応じて、fields = ['movie_id', 'title', 'genres', ...] のように明示的に指定することもできます