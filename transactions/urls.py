from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
	path('', views.index, name = 'index'),
	#path('txn/list/', views.TransactionList.as_view(), name='transaction_list'),
	path('txn/list/', views.index, name = 'transaction_list'),
	path('txn/new/', views.TransactionCreate.as_view(), name='transaction_new'),
	path('txn/view/<int:pk>', views.TransactionView.as_view(), name='transaction_view'),
	path('txn/edit/<int:pk>', views.TransactionUpdate.as_view(), name='transaction_edit'),
	path('txn/delete/<int:pk>', views.TransactionDelete.as_view(), name='transaction_delete'),

	path('farmer/list/', views.farmers, name = 'farmer_list'),
	path('farmer/new/', views.FarmerCreate.as_view(), name='farmer_new'),
	path('farmer/edit/<int:pk>', views.FarmerUpdate.as_view(), name='farmer_edit'),

	path('company/list/', views.companies, name = 'company_list'),
	path('company/new/', views.CompanyCreate.as_view(), name='company_new'),
	path('company/edit/<int:pk>', views.CompanyUpdate.as_view(), name='company_edit'),
]