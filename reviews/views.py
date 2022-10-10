from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.

def index(request):
    pass

def create(request):
    review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/create.html', context)
