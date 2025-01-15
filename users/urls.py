from django.urls import path
from .views import RegisterView, LoginView, ProfileView, AdminOnlyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),  
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only')
]
