from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [


path('', views.index, name='index'),
path('song_list', views.song_list, name='song_list'),

path('chapter/<str:bookname>/<str:chapter>', views.chapter_detail, name='chapter_detail'),
path('verse/<str:bookname>/<str:chapter>/<str:versecount>',views.verse_detail,name='verse_detail'),
path('books/', views.book_list, name='book_list'),  # URL to render the book list
path('get-chapters/<str:bookname>/', views.get_chapters, name='get_chapters'),  # API for fetching chapters


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
