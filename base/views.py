from django.shortcuts import render
from .models import Messages
from .models import BlogPost,Drivers_License,detailed_List,License_Category
from django.contrib import messages


# Create your views here.





def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def blog_page(request):
    upload = BlogPost.objects.all()
    return render(request,'blog.html',{'upload':upload})

def contact_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        body = request.POST.get('body')

        message = Messages.objects.create(username=username, email=email,body=body)
        message.save()
        messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.')

    return render(request,'contact.html')

def faq_page(request):
    return render(request,'faq.html')

def courses_page(request):
    return render(request,'courses.html')


def private_page(request):
    return render(request,'privatepolicy.html')

def terms_page(request):
    return render(request,'Terms.html')

def driver_page(request):
    driver = Drivers_License.objects.all()
    return render(request, 'driverlesson.html',{'driver':driver})


def list_detail(request,slug):
    driver = Drivers_License.objects.get(slug=slug)
    item = driver.license_category_set.all()
    list_item = driver.detailed_list_set.all()
    # driver = License_Category.objects.get(slug)
    context = {'driver':driver,'item':item,'list_item':list_item}
    return render(request, 'adminlicense.html',context)

def Coche_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        body = request.POST.get('body')

        message = Messages.objects.create(username=username, email=email,body=body)
        message.save()
        messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.')
    return render(request,'Coche.html')

def moto_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        body = request.POST.get('body')

        message = Messages.objects.create(username=username, email=email,body=body)
        message.save()
        messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.')
    return render(request,'moto.html')

def conductor_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        body = request.POST.get('body')

        message = Messages.objects.create(username=username, email=email,body=body)
        message.save()
        messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.')
    return render(request,'conductor.html')

def Permisos(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        body = request.POST.get('body')

        message = Messages.objects.create(username=username, email=email,body=body)
        message.save()
        messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.')
    return render(request, 'Permisos.html')

def Vehículos(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        body = request.POST.get('body')

        message = Messages.objects.create(username=username, email=email,body=body)
        message.save()
        messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo lo antes posible.')
    return render(request, 'heavy.html')

