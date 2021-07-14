from django.shortcuts import render, HttpResponse, redirect
from shopApp .models import shopperProduct,ShopperRegistration
from django.contrib.auth.models import User,auth


# Create your views here.
def shopper(request):
    if request.method == 'POST':
        pro_Id  = request.POST['pro_id']
        pro_name = request.POST['pro_name']
        shop_name = request.POST['shop_name']
        pro_desc = request.POST['pro_desc']
        pro_img = request.FILES['pro_img']
        pro_price = request.POST['pro_price']
        pro_sub = shopperProduct(pro_name = pro_name, pro_desc = pro_desc, pro_price = pro_price, pro_img = pro_img, pro_ID = pro_Id, pro_shopName = shop_name)
        pro_sub.save()
        return redirect(shopper)
    return render(request, 'shop_product_post.html')

def shopperRegistrations(request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        shop_name = request.POST['shop_name']
        user_mail = request.POST['user_mail']
        user_mobile = request.POST['user_mobile']
        user_address = request.POST['user_address']
        user_B_date = request.POST['user_B_date']
        user_MBank = request.POST['user_MBank']
        user_img = request.FILES['user_img']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            reg_Data = User.objects.create_user(username=user_name, first_name = shop_name,email=user_mail, password=password1)
            reg_Data.save()
            final_reg_data = ShopperRegistration(user_name = user_name, shop_name = shop_name, user_mail = user_mail , user_mobile = user_mobile, user_address = user_address, user_B_date = user_B_date, user_MBank =user_MBank , user_img =user_img)
            final_reg_data.save()
            return HttpResponse("SAve Data")
        else:
            return HttpResponse('Password Bul')
    else:
        pass
    return render(request, "shopper_regis.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_email = request.POST['user_email']
        password = request.POST['password']
        user = auth.authenticate(username=username,email= user_email,password=password,)


        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return HttpResponse("OI")
    else:

        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



def userAndSeller(request):
    return  render(request, "verify.html")
