from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from .models import Category,Product,Medicines,PharmLab

from .forms import ContactForm,OrderForm
# Create your views here.
def home(request):
    return render (request,'index.html')

def order(request):
    form = OrderForm() 
    if request.method == "POST":
        form = OrderForm(request.POST) 
        if form.is_valid():     
            form.save()
            return render(request ,'thankyou.html')
    dict_form = {
        'form': form
    }
    return render (request,'checkout.html',dict_form)


def about(request):
    return render (request,'about.html')

def category(request):
    dict_cat = {
        'cat': Category.objects.all()
    }
    return render (request,'category.html',dict_cat)

def shop(request):
    dict_pro = {
        'pro': Product.objects.all()
    }
    return render (request,'shop.html',dict_pro)

# from django.shortcuts import render, get_object_or_404

def shop_single(request, pro_name):
    product = get_object_or_404(Product, pro_name=pro_name)
    return render(request, 'shop-single.html', {'p': product})

def cart(request):
    return render (request,'cart.html')

def contact(request):
    form = ContactForm() 
    if request.method == "POST":
        form = ContactForm(request.POST) 
        if form.is_valid():     
            form.save()
            return render(request ,'confirmation.html')
    dict_form = {
        'form': form
    }
    return render (request,'contact.html',dict_form)
    

def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'thankyou.html')
    form = OrderForm()
    dict_form = {
        'form': form
    }
    return render (request,'checkout.html',dict_form)

def thankyou(request):
    return render (request,'thankyou.html')

def pharmlab(request):
    dict_pro = {
        'tests': PharmLab.objects.all()
    }
    return render (request,'pharmlab.html',dict_pro)

def test_single(request,test_name):
    lab_test = get_object_or_404(PharmLab,test_name=test_name)
    return render (request,'test_single.html',{'t':lab_test})

def medicines(request):
    dict_pro = {
        'med': Medicines.objects.all()
    }
    return render (request,'medicines.html',dict_pro)

def med_single(request, med_name):
    medicine = get_object_or_404(Medicines, med_name=med_name)
    return render(request, 'med_single.html', {'m': medicine})

def med_checkout (request):
    return render(request ,'med_checkout.html')



    





# def product(request):
#     dict_pro = {
#         'pro': Product.objects.all()
#     }
#     return render (request,'product.html',dict_pro)
    
def customers(request):
    return render (request,'customers.html')


