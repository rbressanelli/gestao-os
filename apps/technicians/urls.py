from django.urls import path
from apps.technicians import views

app_name = 'technicians'
urlpatterns = [
    path('technicians/', views.Dummy.as_view())
]
