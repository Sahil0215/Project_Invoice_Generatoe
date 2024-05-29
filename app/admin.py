from django.contrib import admin

# Register your models here.


from .models import *  # Import your models here

# Register your models
admin.site.register(item)
admin.site.register(buyer)
admin.site.register(seller)
admin.site.register(bill)