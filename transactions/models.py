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

class Transaction(models.Model):
	date = models.DateTimeField()
	farmer = models.ForeignKey(Farmer, on_delete=models.PROTECT)
	company = models.ForeignKey(Company, on_delete=models.PROTECT)
	farmer_price = models.DecimalField(decimal_places=2, max_digits=8)
	company_price = models.DecimalField(decimal_places=2, max_digits=8)
	quantity = models.DecimalField(decimal_places=2, max_digits=8)
	comment = models.TextField(blank = True)

	def __str__(self):
		return f"{self.name} - {self.location}"

	class Meta:
		ordering = ['date']