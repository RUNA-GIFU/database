from django.contrib import admin

# Register your models here.

from .models import Movie  # Movieモデルをインポート

# Register your models here.
# Movieモデルを管理サイトに登録します
admin.site.register(Movie)