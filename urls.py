# backend/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/hello_db/', include('api.hello_db.urls')),
    path('api/inventory/', include('api.inventory.urls')),
    path('api/movies/', include('api.movies.urls')), 
]