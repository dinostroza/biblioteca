from django.db import models
from books.models import Book
from django.core.validators import MaxValueValidator

import datetime

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

def year_choices():
    return [(r,r) for r in range(datetime.date.today().year,1800,-1)]


class Author(models.Model):
	name  = models.CharField(max_length=45,blank=False,null=False)
	books = models.ManyToManyField(Book,through='Publication')

	def __str__(self):
		return self.name
	
	class Meta:
		db_table = 'author'

class Publication(models.Model):
	author    = models.ForeignKey(Author,blank=False,null=False)
	book      = models.ForeignKey(Book,blank=False,null=False)
	published_year = models.PositiveSmallIntegerField(choices=year_choices(),blank=True,null=True,validators=[max_value_current_year])
	def __str__(self):
		return '%s: %s'%(self.book,self.author)
	
	class Meta:
		db_table = 'publication'
		unique_together=(('author','book'),)
