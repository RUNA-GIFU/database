#config/urls.py

from django.contrib import admin
from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static 

# ← 不要なインポートを削除！
# from api.movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/hello_db/', include('api.hello_db.urls')),
    path('api/inventory/', include('api.inventory.urls')),
    path('api/movies/', include('api.movies.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
