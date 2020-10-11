from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	# localhost:8000/admin
	path('admin/', admin.site.urls),
	# localhost:8000/
	path('',include('hellomobileapp.urls')),
	path('login/', auth_views.LoginView.as_view(template_name='hellomobileapp/login.html'),name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='hellomobileapp/logout.html'),name='logout')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)