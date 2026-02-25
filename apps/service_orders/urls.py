from django.urls import path
from apps.service_orders import views

app_name = 'service_orders'
urlpatterns = [
    path('service_orders/', views.Dummy.as_view())
]
