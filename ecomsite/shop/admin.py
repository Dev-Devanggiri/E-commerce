from django.contrib import admin
from .models import Products, Order


admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "YouCart"
admin.site.index_title = "Manage YouCart"


class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discount_price','category',)
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)
    fields = ('price','category',)
    list_editable = ('price','category',)

# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)