# Create your views here.
from django.shortcuts import render

from .form import ReviewForm


def review(request):
    form = ReviewForm()
    return render(request, 'review/index.html', {
        "form": form
    })
