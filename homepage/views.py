from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from .models import ContactMessages, NewsLetter
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def home_page(request):
    page = 'index.html'
    template = loader.get_template(page)
    menu = []
    for x in range(1,6):
        image = f'images/earlz{x}.jpg'
        menu.append(image)
    context = {'menu': menu}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def order(request):
    page = 'order.html'
    template = loader.get_template(page)
    context = {'email': ''}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def menu(request):
    page = 'menu.html'
    template = loader.get_template(page)
    menu = []
    for x in range(1,7):
        image = f'images/earlz{x}.jpg'
        menu.append(image)
    context = {'menu': menu}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def confirm_order(request):
    page = 'confirm.html'
    template = loader.get_template(page)
    context = {'email': ''}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)

@api_view(['POST'])
def contact(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')

    print(name)
    print(email)
    print(message)
    message = ContactMessages(first_name=name, email=email, message=message)
    message.save()

    page = 'thanks.html'
    template = loader.get_template(page)
    context = {'name': str(name).capitalize()}
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
