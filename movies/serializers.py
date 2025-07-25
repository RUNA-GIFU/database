# backend/api/movies/serializers.py

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    # ↓↓↓ この2行を追加 ↓↓↓
    # movie_posterフィールドから完全なURLを生成するための設定
    movie_poster = serializers.ImageField(use_url=True)

    class Meta:
        model = Movie
        # 以前の長いリストは不要です。これで全て含まれます。
        fields = '__all__'
        # ユーザーが入力しないフィールドは読み取り専用に
        read_only_fields = ['id', 'created_at', 'updated_at']