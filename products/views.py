from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Product
from django.utils import timezone
def home(request):
    product=Product.objects
    return render(request,'products/home.html',{'product':product})
@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.title=request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or  request.POST['url'].startswith('https://') :
                product.url=request.POST['url']
            else:
                product.url='https://'+request.POST['url']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('/products/'+str(product.id))

        else:
            return render(request, 'products/create.html',{'error':'please fill all th fields'})
    else:
        return render(request,'products/create.html')
# Create your views here.
def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'alldetail':product})
@login_required
def upvote(request,product_id):
    if request.method=='POST':
        product=get_object_or_404(Product,pk=product_id)
        product.upvote_total+=1
        product.save()
        return redirect('/products/'+str(product.id))