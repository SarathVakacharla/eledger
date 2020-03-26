from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import Farmer, Company, Transaction
from .forms import CreateFarmer, CreateCompany, CreateTransaction

## Transactions ##
def index(request):
	return render(request, 'transactions/transaction_list.html', {'transactions': Transaction.objects.all()})

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

class TransactionDelete(DeleteView):
	model = Transaction
	fields = '__all__'
	success_url = reverse_lazy('transaction_list')

def farmers(request):
	return render(request, 'transactions/farmer_list.html', {'farmers': Farmer.objects.all()})

## Farmers ##
class FarmerCreate(CreateView):
	model = Farmer
	fields = '__all__'
	success_url = reverse_lazy('farmer_list')

class FarmerUpdate(UpdateView):
	model = Farmer
	fields = '__all__'
	success_url = reverse_lazy('farmer_list')

def companies(request):
	return render(request, 'transactions/company_list.html', {'companies': Company.objects.all()})
	
## Companies ##
class CompanyCreate(CreateView):
	model = Company
	fields = '__all__'
	success_url = reverse_lazy('company_list')

class CompanyUpdate(UpdateView):
	model = Company
	fields = '__all__'
	success_url = reverse_lazy('company_list')

