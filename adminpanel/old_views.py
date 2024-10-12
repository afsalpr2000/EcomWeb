from django.shortcuts import render,get_object_or_404, redirect
from home.models import Product, Category
from django.contrib import messages



# Create your views here.
def admin_home(request):
    product = Product.objects.all()
    return render(request,'adminpanel/index.html',{'products': product})

def add_product(request):
    categories = Category.objects.all()   

    if request.method=='POST':
        name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        prod_image = request.FILES.get('product_image')
        price = request.POST.get('product_price')
        stock = request.POST.get('product_stock')        
        category_id = request.POST.get('product_category')
        category = get_object_or_404(Category,id = category_id)
        Product.objects.create(name = name,
                               description = description,
                               image = prod_image,
                               category = category, 
                               price = price, 
                               stock = stock)
        messages.success(request, "Product created successfully!")
        return redirect('admin_home')
    return render(request,'adminpanel/add_product.html',{'categories':categories})

def edit_product(request,product_id):
    product = get_object_or_404(Product, id = product_id)
    categories = Category.objects.all()
    if request.method =='POST':
        product.name = request.POST.get('product_name')
        product.description = request.POST.get('product_description')
        image = request.FILES.get('product_image')
        product.price = request.POST.get('product_price')
        product.stock = request.POST.get('product_stock')        
        category_id = request.POST.get('product_category')
        category = get_object_or_404(Category,id = category_id)
        product.category = category
        if image:
            product.image = image
        messages.success(request, "Product details updated!")    
        product.save()
        return redirect('admin_home')

    context ={
            'product' : product,
            'categories' : categories,
        }
    return render(request,'adminpanel/edit_product.html',context)

def delete_product(request,product_id):
    product = get_object_or_404(Product, id = product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('admin_home')

    return render(request,'adminpanel/delete_product.html',{'product':product})