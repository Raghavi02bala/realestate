from django.contrib import admin

from .models import Listing

class LsitingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')

admin.site.register(Listing,LsitingAdmin)
