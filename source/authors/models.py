from django.db import models
from books.models import Book
# Create your models here.

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
	
	def __str__(self):
		return '%s: %s'%(self.book,self.author)
	
	class Meta:
		db_table = 'publication'

