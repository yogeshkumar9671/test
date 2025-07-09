from django.contrib import admin
from .models import Profile, Product, CartItem

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'mobile', 'phone')



# for product listing admin panelfrom django.contrib import admin

from django.contrib import admin
from .models import Product




admin.site.register(CartItem)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'price', 'color', 'size')
    list_filter = ('category', 'subcategory', 'color', 'size')
    search_fields = ('title', 'description')

