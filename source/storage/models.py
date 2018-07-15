from django.db import models

class TypeStorage(models.Model):
	name = models.CharField(max_length=64, blank=False, null=False, unique=True)
	description = models.CharField(max_length=256, blank=True, null=True)
	def __str__(self):
		return self.name

	class Meta:
		db_table = 'typestorage'

class StorageUnit(models.Model):
	name        = models.CharField(max_length=128, blank=False, null=False, unique=True)
	stype       = models.ForeignKey(TypeStorage, blank=False, null=False)
	location    = models.ForeignKey('Location', blank=False, null=False)
	description = models.CharField(max_length=256, blank=True, null=True)
	modified    = models.DateTimeField(auto_now=True)	
	created     = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'storageunit'

class Location(models.Model):
	address = models.CharField(max_length=128, blank=False, null=False)
	city    = models.CharField(max_length=128, blank=False, null=False)
	state   = models.CharField(max_length=128, blank=False, null=False)
	room    = models.CharField(max_length=128, blank=False, null=False)
	
	def __str__(self):
		return '%s, %s, %s'%(self.address,self.city,self.state)

	class Meta:
		db_table = 'location'
