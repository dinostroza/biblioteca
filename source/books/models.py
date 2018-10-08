from django.db import models
from isbn_field import ISBNField
from storage.models import StorageUnit
from django.contrib.postgres.fields import JSONField

class Book(models.Model):
	isbn      = ISBNField(unique=True,blank=True,null=True)
	title     = models.CharField(max_length=256, blank=True, null=True)
	subject   = models.ForeignKey('BookSubject',max_length=64, blank=True, null=True)
	edition   = models.PositiveSmallIntegerField(blank=True, null=True)
	description = models.CharField(max_length=64, blank=True, null=True)
	editorial = models.ForeignKey('Editorial',blank=True,null=True)
	num_pages = models.PositiveIntegerField(blank=True, null=True)
	condition = models.ForeignKey('BookCondition', blank=True, null=True)
	extra     = models.CharField(max_length=256, blank=True, null=True)
	index     = JSONField(blank=True, null=True)

	@property
	def matter(self):
		return str(self.subject.matter)

	def author_list(self):
		author_list = self.authors.all()
		str_author_list = ', '.join([a.name for a in author_list])
		return str_author_list

	author_list.short_description = "Authors"


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
	book = models.OneToOneField(Book, blank = False, null=False)
	storeunit = models.ForeignKey(StorageUnit, blank = False, null=False)
	date = models.DateField()

	def __str__(self):
		return '%s: %s'%(self.storeunit,self.book)

	class Meta:
		db_table = 'storagedbook'

class BookCondition(models.Model):
	name        = models.CharField(max_length=64, blank=True, null=True)
	description = models.CharField(max_length=256, blank=True, null=True)
	
	def __str__(self):
		return self.name

	class Meta:
		db_table = 'bookcondition'

class BookSubject(models.Model):
	name        = models.CharField(max_length=64, blank=True, null=True)
	description = models.CharField(max_length=256, blank=True, null=True)
	matter      = models.ForeignKey('BookMatter', blank=True, null=True)
	def __str__(self):
		return '{} - {}'.format(self.matter, self.name)

	class Meta:
		db_table = 'booksubject'

class BookMatter(models.Model):
	name        = models.CharField(max_length=64, blank=True, null=True)
	description = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'bookmatter'