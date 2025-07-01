"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('about', views.about, name='about'),
        path('contact1', views.contact1, name='contact1'),
        path('login', views.login, name='login'),
        path('signup', views.signup, name='signup'),
        path('logout1', views.logout1, name='logout1'),
        path('forgotpassword', views.forgotpassword, name='forgotpassword'),
        path('adduserdetail', views.adduserdetail, name='adduserdetail'),
        path('showuser', views.showuser, name='showuser'),
        path('editprofile', views.editprofile, name='editprofile'),
        path('update', views.update, name='update'),
        path('addseller', views.addseller, name='addseller'),
        path('showseller', views.showseller, name='showseller'),
        path('editsellerdetail', views.editsellerdetail, name='editsellerdetail'),
        path('updateseller', views.updateseller, name='updateseller'),
        path('products', views.products, name='products'),
        path('productdetails/<int:product_id>/', views.productdetails, name='productdetails'),
        path('addproducts', views.addproducts, name='addproducts'),
        path('sellerproduct', views.sellerproduct, name='sellerproduct'),
        path('deleteProduct/<int:eid>', views.deleteProduct, name='deleteservice'),
        path('ecommerce-single/<int:product_id>/', views.productdetails, name='ecommerce-single'),
        path('add_to_cart', views.add_to_cart, name='add_to_cart'),
        path('ecommerce-cart', views.ecommerce_cart, name='ecommerce_cart'),
        path('removefromcart/<int:id>', views.removefromcart, name='removefromcart'),
        path('increaseitem/<int:id>', views.increaseitem, name="increseitem"),
        path('decreaseitem/<int:id>', views.decreaseitem, name="decreseitem"),
        path('update_product_quantity/', views.update_product_quantity, name='update_product_quantity'),
        path('payment-status/', views.success, name='payment_status'),
        path('payment', views.payment, name='payment'),
        path('vieworder/<int:id>', views.vieworder, name='vieworder'),
        path('storefeedback', views.storefeedback, name='storefeedback'),
        path('productfeedback/<int:order_id>', views.productfeedback, name='productfeedback'),
        path('sellershoworder', views.sellershoworder, name='sellershoworder'),
        path('complaint_submit', views.complaint_submit, name='complaint_submit'),


    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

