from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'phone', "role", "status","id_proof","pic")
    search_fields = ('name', 'email')

@admin.register(Contact_detail)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'timestamp')


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'date_of_birth', 'profession','bio','user_image')

@admin.register(SellerProfile)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'seller_image', 'shop_name', "shop_address", "years_of_experience","specialization","rating","availability")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('seller','category','name', 'description', 'price', 'quantity','availability','pic')

@admin.register(productCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'Price', 'Quantity', 'Order_status', 'timeStamp')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature','payment_mode','status','offline_reference','offline_remarks','address')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_id', 'ratings', 'comment', 'timestamp')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user','subject','description','timestamp')
