from django.urls import path

from stuff.views import index

app_name = 'stuff'
urlpatterns = [
    path('', index, name='index'),
]
