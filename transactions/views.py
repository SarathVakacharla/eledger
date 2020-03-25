from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import Farmer, Company, Transaction
from .forms import CreateFarmer, CreateCompany, CreateTransaction

def get_all_actors():
	farmers = Farmer.objects.all()
	companies = Company.objects.all()
	actors = {
		'farmers' : farmers,
		'companies' : companies
	}
	return actors

def index(request):
	return render(request, 'transactions/transaction_list.html', {'transactions': Transaction.objects.all()})

def actors(request):
	return render(request, 'farmers_companies.html', {'actors': get_all_actors()})

def create_farmer(request):
	if request.method == 'POST':
		new_farmer = CreateFarmer(request.POST)
		if new_farmer.is_valid():
			new_farmer.save()
			return redirect('actors')
		else:
			return HttpResponse("""Unable to create farmer, try again <a href = "{{ url : 'actors'}}">reload</a>""") #TODO: give link to create page
	else:
		context = {
			'actors': get_all_actors(),
			'status' : {
				'disposition' : "FAILURE",
				'message' : "Unable to created farmer" #TODO: add farmer name
			}
		}
		return render(request, 'farmers_companies.html', context)

# TODO: update farmers


def create_company(request):
	if request.method == 'POST':
		new_company = CreateCompany(request.POST)
		if new_company.is_valid():
			new_company.save()
			return redirect('actors')
		else:
			return HttpResponse("""Unable to create company, try again <a href = "{{ url : 'actors'}}">reload</a>""") #TODO: give link to create page
	else:
		context = {
			'actors': get_all_actors(),
			'status' : {
				'disposition' : "SUCCESS",
				'message' : "Succesfully created company" #TODO: add ompany name
			}
		}
		return render(request, 'farmers_companies.html', context)

# TODO: update companies

class TransactionList(ListView):
	model = Transaction

class TransactionView(DetailView):
	model = Transaction

class TransactionCreate(CreateView):
	model = Transaction
	fields = '__all__'
	success_url = reverse_lazy('transaction_list')

class TransactionUpdate(UpdateView):
	model = Transaction
	fields = '__all__'
	success_url = reverse_lazy('transaction_list')