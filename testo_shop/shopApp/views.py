from django.shortcuts import render,HttpResponse
from shopApp .models import shopperProduct,topProducts,shopEvent
# Create your views here.
# def shopIndex(request):
#     return render(request, "index.html")



def proDuctView(request):
    topPro = topProducts.objects.all()
    shopperPro = shopperProduct.objects.all()
    event_show = shopEvent.objects.all()
    return render(request, "index.html", {"top_products": topPro , "Seller_products" : shopperPro, "event_show" : event_show})