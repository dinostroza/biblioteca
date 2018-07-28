from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Editorial)
admin.site.register(StoragedBook)
admin.site.register(BookCondition)
admin.site.register(BookSubject)
admin.site.register(BookMatter)
