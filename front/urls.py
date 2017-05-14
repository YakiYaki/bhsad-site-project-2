from django.conf.urls import url
from front import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ru$', views.ru, name='ru'),
    url(r'^en$', views.en, name='en'),
]