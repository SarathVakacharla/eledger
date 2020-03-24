from django import forms
from .models import Farmer, Company

class CreateFarmer(forms.ModelForm):

	class Meta:
		model: Farmer
		fields = '__all__'


class CreateCompany(forms.ModelForm):

	class Meta:
		model: Company
		fields = '__all__'