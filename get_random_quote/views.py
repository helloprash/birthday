from django.shortcuts import render
from django.http import HttpResponse
import requests
import json, os
from random import seed
from random import randint
from get_random_quote.models import Quote

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def get_random_quote(request):
    quote_render = Quote.objects.all()
    value = randint(0, len(quote_render)-1)
    quote_to_render = quote_render[value].quote
    author_to_render = quote_render[value].author
    image_view = Quote.objects.order_by('id')[value]


    data = {
            'quote': quote_to_render,
            'author' : author_to_render,
            'images' : image_view
    }
    return render(request,'random/get_random_quote.html',context=data)

