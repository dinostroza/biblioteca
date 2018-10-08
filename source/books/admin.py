from django.contrib import admin
from .models import *
from authors.models import Publication

class AuthorInline(admin.TabularInline):
	model=Publication
	extra=1

class StoragedInline(admin.TabularInline):
	model=StoragedBook
	extra=1

class BookAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'author_list',
		'subject',
		'num_pages'

	)
	inlines=(
		AuthorInline,
		StoragedInline,
	)



admin.site.register(Book,BookAdmin)
admin.site.register(Editorial)
admin.site.register(StoragedBook)
admin.site.register(BookCondition)
admin.site.register(BookSubject)
admin.site.register(BookMatter)
