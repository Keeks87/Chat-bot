from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('response/', views.chat_response, name='chat_response'),
]
