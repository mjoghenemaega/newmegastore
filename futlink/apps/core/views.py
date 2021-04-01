from django.shortcuts import render

from apps.store.models import Product

def order_confirmation(request):
	return render(request, 'email_confirmation.html')


	

def frontpage(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'frontpage.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')