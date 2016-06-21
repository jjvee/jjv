from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Shop(models.Model):
	name = models.CharField(max_length=30)
	crdate = models.DateTimeField()
	
	def __str__(self):
		return self.name
		
class Menu(models.Model):
	shop = models.ForeignKey(Shop)
	name = models.CharField(max_length=30)
	size = models.CharField(max_length=10)
	price = models.IntegerField(default=0)
	category = models.CharField(max_length=10)
	crdate = models.DateTimeField()
	
	def __str__(self):
		return self.name
	

class Meetings(models.Model):
	mtname = models.CharField(max_length=30)
	mtteam = models.CharField(max_length=30)
	mtdate = models.DateTimeField()
	mtloca = models.CharField(max_length=30)
	mthost = models.CharField(max_length=20)
	mtmemo = models.CharField(max_length=100)
	shop = models.ForeignKey(Shop, null=True, blank=True, default = None)
	crdate = models.DateTimeField()
	
	def __str__(self):
		return self.mtname
		
class Order(models.Model):
	meeting =  models.ForeignKey(Meetings, null=True, blank=True, default = None)
	membername = models.CharField(max_length=30)
	menu = models.ForeignKey(Menu, null=True, blank=True, default = None)
	quantity = models.IntegerField(default=0)
	amount = models.IntegerField(default=0)
	note = models.CharField(max_length=100)
	crdate = models.DateTimeField()
	
	def __str__(self):
		text = self.membername + ' / ' + self.menu.name
		return text