from django.conf.urls import url
from . import views

app_name='grade'
urlpatterns = [
    url(r'^$', views.ensalamento),
    url(r'^teste', views.teste, name='teste'),
]
