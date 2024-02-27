from django.urls import path

from . import views

urlpatterns = [
    path('', views.models_list),
    path('html', views.post_list),
]
