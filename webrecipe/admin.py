from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_title="Share Food Recipe"
admin.site.site_header='Simple Recipe'
admin.site.index_title='Recipe'

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','address','phone_number')
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=('category',)
    search_fields=('category',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product','description','price','category')
    search_fields=('product','category','price')    

    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('product','order_date','customer','total_amount','status')
    search_fields=('product',)    
     
    

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','quantity','price')
    search_fields=('order',)    
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('creation_date','product')
    search_fields=('order',)     
    
@admin.register(Payment)
class PayementAdmin(admin.ModelAdmin):
    list_display=('payment_id','customer','order','payment_date','amount','payment_method','transaction_id')
    search_fields=('payment_id',)        
     
    
      
    
