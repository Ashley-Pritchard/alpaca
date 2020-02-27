from django.urls import path
from . import views

#urls - each corresponds to both a html page and a function in the views.py file 

urlpatterns = [
    path('', views.index, name='index'),
    path('/search', views.search, name='search'),
    path('/import_variant', views.import_variant, name='import_variant'),
    path('/imported', views.imported, name='imported')
]
