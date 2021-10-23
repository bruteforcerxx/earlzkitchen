from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from .models import ContactsMessages, NewsLetter
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def home_page(request):
    page = 'index.html'
    template = loader.get_template(page)
    menu = []
    for x in range(1,4):
        item = {"food": f"Food{x}", "price": "2000", "image":  f'images/earlz{x}.jpg', "item_num": x, "desc": f"food description here"}
        menu.append(item)
    context = {'menu': menu}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def order(request, item):
    page = 'order.html'
    template = loader.get_template(page)
    item = {"brand": f"Food{item}", "price": "2000", "image": f'images/earlz{item}.jpg', "item_num": item}
    context = {'item': item}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def menu(request):
    page = 'menu.html'
    template = loader.get_template(page)
    menu = []
    for x in range(1,7):
        item = {"food": f"Food{x}", "price": "2,000", "image":  f'images/earlz{x}.jpg',  "item_num": x,
                "desc": f"food description here"}
        menu.append(item)
    context = {'menu': menu}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['POST'])
def confirm_order(request, item):
    page = 'confirmorder.html'
    template = loader.get_template(page)
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    quantity = request.POST.get('quantity', '')
    address = request.POST.get('address', '')
    food = f'food{item}'
    price = '2,000'
    details = {'name': name, 'phone': phone, 'quantity': quantity, 'address': address, 'food': food,
               'price': price, 'item_num': item}
    context = {'details': details}
    print(context)
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def purchase_thanks(request):
    page = 'purchase_thanks.html'
    template = loader.get_template(page)
    image = f'images/earlz1.jpg'
    context = {'image': image}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['POST'])
def contact(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')

    print(name)
    print(email)
    print(message)
    message = ContactsMessages(first_name=name, email=email, message=message)
    message.save()

    page = 'contact_thanks.html'
    template = loader.get_template(page)
    context = {'name': str(name).capitalize()}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def contact_thanks(request):
    page = 'contact_thanks.html'
    template = loader.get_template(page)
    image = f'images/earlz1.jpg'
    context = {'image': image}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def sitemap(request):
    page = 'sitemap.xml'
    template = loader.get_template(page)
    return HttpResponse(template.render({'header': 'TESTING ABOUT VIEW'}, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def google(request):
    page = 'googled968c7bfc1d91ec1.html'
    template = loader.get_template(page)
    return HttpResponse(template.render({'header': 'TESTING ABOUT VIEW'}, request), status=status.HTTP_200_OK)
