from django.contrib import admin

from .models import Bookings, Menu

# Register your models here.
admin.site.register(Menu)
admin.site.register(Bookings)