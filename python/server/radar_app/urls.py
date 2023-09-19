from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('__admin__/', views.__admin__, name='__admin__'),
    path('error/', views.error, name='error'),
]

