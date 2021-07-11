from django.shortcuts import render, HttpResponse, redirect
from shopApp .models import ShopperRegistration,shopperProduct,topProducts,shopEvent

# def shopadmin(request):
#     return render(request, "shopAdmin.html")


def shopperProductsShow(request):
    adminPanelProducts = shopperProduct.objects.all()
    top_p = topProducts.objects.all()
    all_seller = ShopperRegistration.objects.all()
    event_pub = shopEvent.objects.all()
    return render(request, "shopAdmin.html", {"showProducts" : adminPanelProducts,"top_pro_show" : top_p, "our_all_seller" : all_seller, "event" : event_pub})


def productDelete(request,id):
    getProId = shopperProduct.objects.get(id=id)
    getProId.delete()
    return redirect('/')

def productUpdate(request,id):
    get_Pro_Details = shopperProduct.objects.get(id=id)
    if request.method == 'POST':
        pro_Id  = request.POST['pro_id']
        pro_name = request.POST['pro_name']
        shop_name = request.POST['shop_name']
        pro_desc = request.POST['pro_desc']
        pro_img = request.FILES['pro_img']
        pro_price = request.POST['pro_price']
        pro_sub = shopperProduct(pro_name = pro_name, pro_desc = pro_desc, pro_price = pro_price, pro_img = pro_img, pro_ID = pro_Id, pro_shopName = shop_name)

        update = get_Pro_Details
        update.delete()
        pro_sub.save()
        return redirect('/')
    return render(request, "update.html" , {"product_Update" : get_Pro_Details})

def topProduct(request,id):
    get_Pro_Details = shopperProduct.objects.get(id=id)
    if request.method == 'POST':
        pro_Id = request.POST['pro_id']
        pro_name = request.POST['pro_name']
        shop_name = request.POST['shop_name']
        pro_desc = request.POST['pro_desc']
        pro_img = request.FILES['pro_img']
        pro_price = request.POST['pro_price']
        pro_sub = topProducts(pro_name=pro_name, pro_desc=pro_desc, pro_price=pro_price, pro_img=pro_img,
                                 pro_ID=pro_Id, pro_shopName=shop_name)


        pro_sub.save()
        return redirect('/')
    return render(request, "update.html", {"product_Update": get_Pro_Details})

def deleteTop(request, id):
    top_p = topProducts.objects.get(id = id)
    top_p.delete()
    return redirect('/')


def shop_Event(request):
    if request.method == "POST":
        Ev_name = request.POST['e_name']
        Ev_desc = request.POST['e_desc']
        Ev_Date = request.POST['e_date']
        Ev_img = request.FILES['e_img']
        event_pub = shopEvent(Ev_name = Ev_name, Ev_desc = Ev_desc, Ev_Date = Ev_Date, Ev_Img = Ev_img)
        event_pub.save()
        return HttpResponse("Save")
    return render(request, "eventRegistrations.html")
def deleteEvent(request, id):
    event = shopEvent.objects.get(id = id)
    event.delete()
    return redirect('/')

