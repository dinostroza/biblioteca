from django.contrib import admin
from .models import Book, Editorial, StoragedBook

admin.site.register(Book)
admin.site.register(Editorial)
admin.site.register(StoragedBook)
