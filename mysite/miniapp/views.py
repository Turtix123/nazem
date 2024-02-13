
from django.http import HttpResponse

import random

def models_list(request):
    random_number = random.randint(1,100)

    return HttpResponse(f"random number {random_number}")
