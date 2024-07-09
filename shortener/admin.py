from django.contrib import admin

# Register your models here.
from .models import URL

class URLAdmin(admin.ModelAdmin):
    list_display = ['id', 'long_url', 'short_url', 'created', 'user_id']
    ordering = ['id']

admin.site.register(URL, URLAdmin)
