from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def orders(request):
    page = 'pendingorders.html'
    template = loader.get_template(page)
    orders = [1, 2, 3, 4, 5, 6, 7, 8]
    context = {'orders': orders}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def confirmed_orders(request):
    page = 'confirmedorders.html'
    template = loader.get_template(page)
    orders = [1, 2, 3, 4, 5, 6, 7, 8]
    context = {'orders': orders}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)



@api_view(['GET'])
def menu(request):
    page = 'additem.html'
    template = loader.get_template(page)
    context = {'email': ''}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)

@api_view(['GET'])
def login(request):
    page = 'login.html'
    template = loader.get_template(page)
    context = {'email': ''}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def add_item(request):
    page = 'additem.html'
    template = loader.get_template(page)
    context = {'email': ''}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['POST'])
def upload_item(request):
    name = request.POST.get('name', '')
    price = request.POST.get('price', '')
    comp = request.POST.get('composition', '')
    category = request.POST.get('category', '')
    image = request.POST.get('image', '')

    page = 'thanks.html'
    template = loader.get_template(page)
    context = {'name': ''}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


