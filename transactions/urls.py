from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
	path('', views.index, name = 'index'),
	path('Create-Farmer/', views.create_farmer, name = 'create-farmer'),
	path('Create-Company/', views.create_company, name = 'create-company')
	#path('update/<int:book_id>', views.update_book),
]