from django.urls import path
from . import views


urlpatterns = [
    path('',views.dependantfield,name='dependant-field')
]
