from django.shortcuts import render,redirect
from .forms import ProductAddForm
from django.contrib import messages
from .models import ProductDetail
from django.contrib.auth.decorators import login_required
# from Product.models import ProductDetail





def AddProduct(request):
    form = ProductAddForm()
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.merchant = request.user
            product.save()
            messages.info(request,"Product Added To List")
            return redirect('AddProduct')
    return render(request,"addproduct.html",{"form":form})

def ProductViewMerchant(request):
    product = ProductDetail.objects.all()
    context = {
        "products":product
    }
    return render(request,"productlist.html",context)

def DeleteProduct(request,pk):
    product = ProductDetail.objects.get(Product_Id = pk)
    product.Product_Image.delete()
    product.delete()
    messages.info(request,"Product Deleted")
    return redirect("ProductViewMerchant")



def UpdateProduct(request,pk):
    product = ProductDetail.objects.filter(Product_Id = pk)
    if request.method == "POST":
        pname=request.POST['pname']
        pbrand=request.POST['pbrand']
        pdescription=request.POST['pdescription']
        pstock=request.POST['pstock']
        pcategory=request.POST['pcategory']
        image=request.FILES['image']

        item=ProductDetail.objects.get(Product_Id=pk)

        item.Product_Name=pname
        item.Product_Brand=pbrand
        item.Product_Description=pdescription
        item.Product_Stock=pstock
        item.Product_Category=pcategory
        item.Product_Image.delete()
        item.Product_Image=image
        item.save()
        messages.info(request,"item updated")

        return redirect("UpdateProduct",pk=pk)
    context = {
        "products":product
    }
    return render(request,"updateproduct.html",context)

@login_required(login_url="SignIn")
def ViewProduct(request,pk):
    Product=ProductDetail.objects.filter(Product_Id=pk)
    context={
        "products":Product
    }
    return render(request,"viewproduct.html",context)
