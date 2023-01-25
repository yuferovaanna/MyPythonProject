from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('relevance', views.index),
    path('geography', views.index),
    path('skills', views.index),
    path('vacancies', views.index)
]
