from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices,state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices
    }
    return render(request,'pages/index.html', context)

def realtor(request,listing_id):
    return render (request,'listings/listing.html')

def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request,'pages/about.html',context)



