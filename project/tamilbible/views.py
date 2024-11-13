# views.py
from django.shortcuts import render, redirect
from .models import BilbleDb

def index(request):
    if request.method == "POST":
        bookname = request.POST.get("Bookname")
        chapter = request.POST.get("Chapter")
        versecount = request.POST.get("Versecount")

        # Filter the queryset based on search criteria
        results = BilbleDb.objects.filter(
            bookname=bookname,
            chapter=chapter,
            versecount=versecount
        )

        # Render the search results template if there are results
        return render(request, 'search_results.html', {
            'results': results,
            'bookname': bookname,
            'chapter': chapter,
            'versecount': versecount,
        })

    # Render the search form template if no search criteria are provided
    book_names = BilbleDb.objects.values_list('bookname', flat=True).distinct()
    return render(request, 'index.html', {'book_names': book_names})



from django.http import JsonResponse
from django.shortcuts import render
from .models import BilbleDb

# View for displaying all books (song names) with a dynamic chapter load
def book_list(request):
    books = BilbleDb.objects.values('book', 'bookname', 'tamilname').distinct()
    return render(request, 'book_list.html', {'books': books})

# API view to get chapters for a specific book
def get_chapters(request, bookname):
    chapters = BilbleDb.objects.filter(bookname=bookname).values('chapter').distinct()
    chapter_list = [chapter['chapter'] for chapter in chapters]
    return JsonResponse({'chapters': chapter_list})






from django.shortcuts import render
from .models import BilbleDb

def song_list(request):
    # Retrieve distinct song names (bookname)
    songs = BilbleDb.objects.values('bookname').distinct()
    chapters = None
    songname = None
    chapters = BilbleDb.objects.all()
    return render(request, 'song_list.html', {'chapters': chapters})

def chapter_detail(request,bookname,chapter):

    # Get the verses related to the selected chapter
    verses = BilbleDb.objects.filter(bookname=bookname,chapter=chapter)

    return render(request, 'chapter_detail.html', {"verses":verses})


def verse_detail(request,bookname,chapter,versecount):

    # Get the specific verse details
    verse_details = BilbleDb.objects.filter(bookname=bookname, chapter=chapter, versecount=versecount)

    return render(request, 'verse_detail.html', {"verse_details":verse_details})
