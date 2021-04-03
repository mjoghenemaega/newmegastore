from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
import random
from .models import Product, Category, ProductReview

def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products
    }

    return render(request, 'search.html', context)

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)


        # Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', category_slug=category_slug, slug=slug)

    #



    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))

    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)

    if product.parent:
        return redirect('product_detail', category_slug=category_slug, slug=product.parent.slug)



    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," %(product.thumbnail.url, product.image.url)


    for image in product.images.all():
        imagesstring =imagesstring + "{'thumbnail': '%s', 'image': '%s'}," %(image.thumbnail.url, image.image.url)

    context = {
        'product': product,
        'imagesstring' : imagesstring,
        'related_products': related_products


    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent=None)


    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)