# admin.py
from django.contrib import admin
from .models import BilbleDb

class BilbleDbAdmin(admin.ModelAdmin):
    list_display = ('book', 'bookname', 'tamilname', 'chapter', 'versecount', 'verse', 'kjv')
    search_fields = ('book', 'bookname', 'tamilname', 'chapter', 'verse')
    list_filter = ('book', 'chapter')

admin.site.register(BilbleDb, BilbleDbAdmin)
