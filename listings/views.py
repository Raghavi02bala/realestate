from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # filter(is_published=True) adding this will make sure , only the published lists are shown.
# paginator is a var.
    paginator = Paginator(listings,3) 
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing , pk=listing_id)
    
    context = {
        'listing' : listing
    }
    return render (request,'listings/listing.html',context)                                                    

def search(request):
    return render(request,'listings/search.html')

# Create your views here.
