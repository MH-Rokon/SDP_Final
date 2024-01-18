
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,UserBookAccountUpdateView
from . import views
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBookAccountUpdateView.as_view(), name='profile' ),
    path('mybook/', views.mybook,name="mybook"),
]