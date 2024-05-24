from django.urls import path
from . import views

urlpatterns=[
    path('json1',views.json1,name="json1"),
    path('',views.data,name="data")
]