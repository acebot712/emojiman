from django.shortcuts import render
from django.http import HttpResponse
import json
from .ai import handle_request


# Create your views here.
def index(request):
    movie = request.GET["movie"]
    emoticons = handle_request(movie)
    # emoticons = response.choices[0].text
    return HttpResponse(f"<html><body>For the movie: {movie} the emoticons are: {emoticons}</body></html>")
