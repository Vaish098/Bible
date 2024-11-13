# models.py
from django.db import models

class BilbleDb(models.Model):
    book = models.CharField(max_length=100)
    bookname = models.CharField(max_length=100)
    tamilname = models.CharField(max_length=10)
    chapter = models.CharField(max_length=100)  # Format "1:1", "2:10", etc.
    versecount = models.CharField(max_length=100)
    verse = models.CharField(max_length=100)
    kjv = models.CharField(max_length=100)

    
    
