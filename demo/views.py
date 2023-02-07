from django.shortcuts import render
from django.http import HttpResponse
from .ai import response


# Create your views here.
def index(request):
    movie = request.GET["movie"]
    emoticons = response.choices[0].text
    return HttpResponse(f"<html><body>For the movie: {movie} the emoticons are: {emoticons}</body></html>")
