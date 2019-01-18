from django.conf.urls import url
from rango import views

urlpatters = [
    url(r'^$, view.index, name = 'index'),
]
