from django.contrib import admin
from .models import Pet
from cart.models import Cart
from django.utils.html import format_html
from orders.models import Oreders,Payment,OrderPet

class OrderCustom(admin.ModelAdmin):
    list_display = ['user','status']

class PaymentCustom(admin.ModelAdmin):
    list_display = ['payment_id','status']



class CustomAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','description','img_display']
    list_filter = ['gender','species']
    search_fields = ['species']

    def img_display(self,obj):
        return format_html('<img src="{}" width="90" height="100"/>',obj.image.url)

# Register your models here.

admin.site.register(Pet,CustomAdmin)
admin.site.register(Oreders,OrderCustom)
admin.site.register(Payment,PaymentCustom)
admin.site.site_header = "Pet Store Admin Panel"
admin.site.site_title = "Welcome to Pet Store Admin"
admin.site.index_title = "Pet App Admin"
