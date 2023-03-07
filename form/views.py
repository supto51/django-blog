# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import ReviewForm


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('review/thank-you')
    else:
        form = ReviewForm()
    return render(request, 'review/index.html', {
        "form": form
    })


def thank_you(request):
    return render(request, 'review/thank-you.html')
