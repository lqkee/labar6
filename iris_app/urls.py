gfrom django.urls import path
from . import views

urlpatterns = [
    path('', views.show_form, name='show_form'),
    path('form/', views.show_form, name='show_form'),
    path('predict/', views.predict, name='predict'),
]
