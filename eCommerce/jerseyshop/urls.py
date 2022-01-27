from django.urls import path, include

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('register', views.register, name="register"),
	path('login', views.login, name="login"),
	path("logout", views.logout, name="logout"),
	path('club/', views.club, name="club"),
	path('country/', views.country, name="country"),
	path('search_results/', views.search_results, name="search_results"),
	path('country/<int:national_jersey_id>/', views.national_jersey_details, name="national_jersey_details"),
	path('club/<int:club_jersey_id>/', views.club_jersey_details, name="club_jersey_details"),
	path('cart/', views.cart, name="cart"),
	path('delete/<int:id>/', views.delete, name="delete"),
	path('checkout/', views.checkout, name="checkout"),
	path('process_order/', views.processOrder, name="process_order"),


	# path('update_item/', views.updateItem, name="update_item"),
]