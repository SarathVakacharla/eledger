from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
	path('', views.index, name = 'index'),
	path('farmcomp/', views.actors, name = 'actors'),
	#path('txn/list/', views.TransactionList.as_view(), name='transaction_list'),
	path('txn/list/', views.index, name = 'transaction_list'),
	path('txn/new/', views.TransactionCreate.as_view(), name='transaction_new'),
	path('txn/view/<int:pk>', views.TransactionView.as_view(), name='transaction_view'),
	path('txn/edit/<int:pk>', views.TransactionUpdate.as_view(), name='transaction_edit'),
	#path('Create-Farmer/', views.create_farmer, name = 'create-farmer'),
	#path('Create-Company/', views.create_company, name = 'create-company')
]