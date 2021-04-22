from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . choices import price_choices, catagory

from .models import Food



def index(request):
    listings = Food.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listing/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Food, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listing/listing.html', context)

def search(request):
    queryset_list = Food.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)


    #   Catagory
    if 'catagory' in request.GET:
        catagory = request.GET['catagory']
        if catagory:
            queryset_list = queryset_list.filter(catagory__iexact=catagory)

    #   Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'catagory': catagory,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listing/search.html', context)