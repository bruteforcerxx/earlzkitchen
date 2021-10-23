from django.contrib import admin
from .models import ContactsMessages, NewsLetter
# Register your models here.

admin.site.register(ContactsMessages)
admin.site.register(NewsLetter)
