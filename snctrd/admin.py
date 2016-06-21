from django.contrib import admin

from .models import Meetings, Shop, Menu, Order
# Register your models here.

admin.site.register(Meetings)
admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Order)