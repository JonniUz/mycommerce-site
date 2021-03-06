from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=225, null=True)
	phone = models.CharField(max_length=225, null=True)
	email = models.CharField(max_length=225, null=True)
	profile_pic = models.ImageField(default = "Madeira_Logo.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add = True, null=True)

	def __str__(self):
		return self.name




class Tag(models.Model):
	name = models.CharField(max_length=225, null=True)

	def __str__(self):
		return self.name




class Product(models.Model):
	CATEGORY = (
		('Indoor', 'Indoor'),
		('Out Door', 'Out Door'),
		)

	name = models.CharField(max_length=225, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=225, null=True, choices=CATEGORY)
	description = models.CharField(max_length=225, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add = True, null=True)
	tags = models.ManyToManyField(Tag)


	def __str__(self):
		return self.name



class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered'),
		)

	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add = True, null=True)
	status = models.CharField(max_length=225, null=True, choices=STATUS)
	note = models.CharField(max_length=225, null=True, blank= True)


	def __str__(self):
		return self.product.name
