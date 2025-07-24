#backend/api/movies/models.py
# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='タイトル')
    genres = models.CharField(max_length=200, blank=True, null=True, verbose_name='ジャンル')
    director = models.CharField(max_length=100, blank=True, null=True, verbose_name='監督')
    actors = models.CharField(max_length=300, blank=True, null=True, verbose_name='俳優')
    release_year = models.IntegerField(blank=True, null=True, verbose_name='公開年')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='制作国')
    #movie_poster_url = models.URLField(max_length=300, blank=True, null=True, verbose_name='ポスターURL')
    movie_poster = models.ImageField(upload_to='posters/', blank=True, null=True, verbose_name='ポスター画像')
    rating = models.FloatField(blank=True, null=True, verbose_name='評価')
    impressions = models.TextField(blank=True, null=True, verbose_name='感想')
    watch_method = models.CharField(max_length=100, blank=True, null=True, verbose_name='視聴方法')
    watched_date = models.DateField(blank=True, null=True, verbose_name='視聴日')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '映画'