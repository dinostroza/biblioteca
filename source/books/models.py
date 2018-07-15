from django.db import models
from isbn_field import ISBNField
from storage.models import StorageUnit

class Book(models.Model):
	isbn      = ISBNField(unique=True)
	title     = models.CharField(max_length=256, blank=True, null=True)
	topic     = models.CharField(max_length=64, blank=True, null=True)
	subtopic  = models.CharField(max_length=64, blank=True, null=True)
	edition   = models.CharField(max_length=64, blank=True, null=True) 
	editorial = models.ForeignKey('Editorial',null=True)
	
	def __str__(self):
		return self.title
	
	class Meta:
		db_table = 'book'

class Editorial(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True)
	
	def __str__(self):
		return self.name

	class Meta:
		db_table = 'editorial'

class StoragedBook(models.Model):
	book = models.ForeignKey(Book, blank = False, null=False)
	storeunit = models.ForeignKey(StorageUnit, blank = False, null=False)
	date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return '%s storaged in %s'%(self.book,self.storeunit)

	class Meta:
		db_table = 'storagedbook'
