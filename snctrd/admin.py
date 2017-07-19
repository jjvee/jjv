from django.contrib import admin

from .models import Meetings, Shop, Menu, Order, Member, Team
# Register your models here.

admin.site.register(Meetings)
admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Member)
admin.site.register(Team)