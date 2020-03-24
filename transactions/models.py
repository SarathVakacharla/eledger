from django.db import models

class Farmer(models.Model):
	name = models.CharField(max_length = 150)
	location = models.CharField(max_length = 150)
	phone = models.CharField(max_length = 13, blank = True)
	email = models.EmailField(blank = True)
	describe = models.TextField(blank = True)
	def __str__(self):
		return f"{self.name} - {self.location}"

class Company(models.Model):
	name = models.CharField(max_length = 150)
	location = models.CharField(max_length = 150)
	phone = models.CharField(max_length = 13, blank = True)
	email = models.EmailField(blank = True)
	describe = models.TextField(blank = True)
	def __str__(self):
		return f"{self.name} - {self.location}"
	