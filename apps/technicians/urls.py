from django.urls import path
from apps.technicians import views

app_name = 'technicians'

urlpatterns = [
    path('technicians/<str:technician_id>/', views.TechnicianView.as_view()),
    path('technicians/', views.TechnicianView.as_view())
]
