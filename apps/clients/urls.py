from django.urls import path
from apps.clients import views

app_name = 'client'
urlpatterns = [
    path('clients/', views.Dummy.as_view())
]
