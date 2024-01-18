
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from .views import HomeView  # Import the HomeView
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('doctor/', include('doctor.urls')),
    path('', HomeView.as_view(), name='home'),   
    path('doctor', views.book, name="doctor"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('appointment/', include('appointment.urls')),
    path('heart/', views.it, name='it'),
    path('medicine/', views.tragedy, name='tragedy'),
    path('child/', views.drama, name='drama'),
    path('all/', views.all, name='ALL'),
    path('patient/', views.pa, name='pa'),
  



  
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)