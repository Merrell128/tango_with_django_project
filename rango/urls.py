from django.conf.urls import url
from rango import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # here "$" is a blank in the website name
    url(r'^about', views.about, name='about'),

]
