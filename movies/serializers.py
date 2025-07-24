from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
  
  # 視聴日フィールドの入力フォーマットを明示的に指定
    watched_date = serializers.DateField(
        format="%Y-%m-%d", 
        input_formats=['%Y-%m-%d', 'iso-8601'], 
        required=False, 
        allow_null=True
    )
    
    class MovieSerializer(serializers.ModelSerializer):
    # movie_posterフィールドから完全なURLを生成するための設定
      movie_poster = serializers.ImageField(use_url=True)
  
    class Meta:
        model = Movie
        #fields = '__all__'
        fields = [
            'id',
            'title',
            'genres',
            'director',
            'actors',
            'release_year',
            'country',
            'movie_poster',
            'rating',
            'impressions',
            'watch_method',
            'watched_date',
            'created_at',
            'updated_at',
        ]
        # ユーザーが入力しないフィールドは読み取り専用にします
        read_only_fields = ['id', 'created_at', 'updated_at']