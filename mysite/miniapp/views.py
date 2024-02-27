
from django.http import HttpResponse

from django.shortcuts import render

import random

def models_list(request):
    random_number = random.randint(1,100)

    return HttpResponse(f"random number {random_number}")

def post_list(request):
    return render(request, 'miniapp/Novy1.html', {})
