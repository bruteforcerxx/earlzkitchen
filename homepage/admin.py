from django.contrib import admin
from .models import ContactMessages, NewsLetter
# Register your models here.

admin.site.register(ContactMessages)
admin.site.register(NewsLetter)
