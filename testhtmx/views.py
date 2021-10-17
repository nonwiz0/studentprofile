from django.shortcuts import render, HttpResponse, redirect
from .forms import BookFormSet
from .models import Author, Book

# Create your views here.
def my_view(req):
    print(req)
    if req.htmx:
        template_name = "testhtmx/partial.html"
    else:
        template_name = "testhtmx/complete.html"
    return render(req, template_name)

def create_book(req, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    formset = BookFormSet(req.POST or None)

    if req.method == 'POST':
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("htmx:create-book", pk=author.id)
    context = {
        "formset": formset,
        "author": author,
        "books": books
    }

    return render(req, "testhtmx/create_book.html", context)

