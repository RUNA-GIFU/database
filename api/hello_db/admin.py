from django.contrib import admin

# Register your models here.

from .models import Hello  # この行を追加

# Register your models here.
admin.site.register(Hello) # この行を追加