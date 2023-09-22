from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sorter_name = request.GET.get('sort')

    if sorter_name == 'name':
        phones = Phone.objects.order_by('name').all()
    elif sorter_name == 'min_price':
        phones = Phone.objects.order_by('price').all()
    elif sorter_name =='max_price':
        phones = Phone.objects.order_by('price').reverse().all()
    else:
        phones = Phone.objects.all()

    context = {'phones': [phone for phone in phones]}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
