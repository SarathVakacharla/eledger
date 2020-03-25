from django.shortcuts import render, redirect
from .models import Farmer, Company
from .forms import CreateFarmer, CreateCompany
from django.http import HttpResponse

def get_all_actors():
	farmers = Farmer.objects.all()
	companies = Company.objects.all()
	actors = {
		'farmers' : farmers,
		'companies' : companies
	}
	return actors

def index(request):
	return render(request, 'farmers_companies.html', {'actors': get_all_actors()})

def create_farmer(request):
	#upload = CreateFarmer()
	if request.method == 'POST':
		new_farmer = CreateFarmer(request.POST)
		if new_farmer.is_valid():
			new_farmer.save()
			return redirect('index')
		else:
			return HttpResponse("""Unable to create farmer, try again <a href = "{{ url : 'index'}}">reload</a>""") #TODO: give link to create page
	else:
		context = {
			'actors': get_all_actors(),
			'status' : {
				'disposition' : "SUCCESS",
				'message' : "Succesfully created farmer" #TODO: add farmer name
			}
		}
		return render(request, 'farmers_companies.html', context)

# TODO: update and delete farmers

def create_company(request):
	#upload = CreateCompany()
	if request.method == 'POST':
		new_company = CreateCompany(request.POST)
		if new_company.is_valid():
			new_company.save()
			return redirect('index')
		else:
			return HttpResponse("""Unable to create company, try again <a href = "{{ url : 'index'}}">reload</a>""") #TODO: give link to create page
	else:
		context = {
			'actors': get_all_actors(),
			'status' : {
				'disposition' : "SUCCESS",
				'message' : "Succesfully created company" #TODO: add ompany name
			}
		}
		return render(request, 'farmers_companies.html', context)

# TODO: update and delete companies