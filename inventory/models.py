from django.db import models

# Create your models here.


# backend/your_app_name/models.py
from django.db import models
import uuid # UUIDを自動生成するために必要

class Meta:
        db_table = 'movies'

# class Movie(models.Model):
#     """
#     映画の鑑賞記録モデル
#     """
#     movie_id = models.CharField(
#         max_length=255,
#         primary_key=True,
#         default=uuid.uuid4, # UUIDを自動生成
#         editable=False, # Django管理画面などで編集不可にする
#         verbose_name='映画ID'
#     )
#     title = models.CharField(max_length=255, verbose_name='タイトル')
#     genres = models.TextField(null=True, blank=True, verbose_name='ジャンル') # カンマ区切り文字列を想定
#     director = models.CharField(max_length=255, null=True, blank=True, verbose_name='監督')
#     actors = models.TextField(null=True, blank=True, verbose_name='俳優') # カンマ区切り文字列を想定
#     release_year = models.IntegerField(null=True, blank=True, verbose_name='公開年')
#     country = models.CharField(max_length=255, null=True, blank=True, verbose_name='制作国')
#     movie_poster_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='ポスター画像URL')
#     rating = models.IntegerField(null=True, blank=True, verbose_name='評価') # 1〜5の整数値
#     impressions = models.TextField(null=True, blank=True, verbose_name='感想')
#     watched_date = models.DateField(verbose_name='視聴日') # 必須項目
#     watch_method = models.CharField(max_length=50, null=True, blank=True, verbose_name='視聴方法')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時') # レコード作成時に自動設定
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時') # レコード更新時に自動更新

    # class Meta:
    #     db_table = 'movies' # データベースのテーブル名を明示的に指定
    #     verbose_name = '映画'
    #     verbose_name_plural = '映画' # 複数形

    # def __str__(self):
    #     return self.title
