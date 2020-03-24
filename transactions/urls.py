from django.urls import path
from . import views
from eledger.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
	path('', views.index, name = 'index'),
	path('Create-Farmer/', views.create_farmer, name = 'create-farmer'),
	path('Create-Company/', views.create_company, name = 'create-company')
	#path('update/<int:book_id>', views.update_book),
]

if DEBUG:
	urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
	urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
