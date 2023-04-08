from django.urls import path

from . import views

app_name = 'personal'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('kategorie/<int:pk>/', views.categoryIndex, name='categoryIndex')
]
