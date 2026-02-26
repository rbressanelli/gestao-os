from django.urls import path
from apps.clients import views

app_name = 'client'

urlpatterns = [
    path('clients/<str:client_id>/', views.ClientView.as_view()),
    path('clients/', views.ClientView.as_view())
]
