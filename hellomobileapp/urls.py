from django.urls import path
from .views import *

urlpatterns = [
	path('', HomePage, name='home-page'),
	path('about/', AboutPage, name='about-page'),
	path('contact/', ContactUs, name='contact-page'),
	path('price/', ShowPrice, name='price-page'),
	path('register/', Register, name='register-page'),
	path('search/', SearchCustomer, name='search-page'),
	path('profile/', EditProfile, name='edit-profile'),
	path('document/', ShowDocument, name='document-page'),
	path('priceinput/', InputPrice, name='priceinput-page')
]