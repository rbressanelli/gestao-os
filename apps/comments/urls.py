from django.urls import path
from apps.comments import views

app_name = 'comments'
urlpatterns = [
    path('comments/', views.Dummy.as_view())
]
