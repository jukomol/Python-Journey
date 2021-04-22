from django.shortcuts import render

# Create your views here.
from food_items.models import Food


def index(request):
    listings = Food.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'listings': listings
    }
    return render(request,'index.html',context)

def menu(request):
    listings = Food.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'listings': listings
    }
    return render(request,'index.html')
def about(request):
    return render(request,'about.html',{})
