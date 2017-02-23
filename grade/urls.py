from django.conf.urls import url
from . import views

app_name='grade'
urlpatterns = [
    url(r'^$', views.ensalamento),
    url(r'^Grade', views.grade, name='grade'),
    url(r'^Cursos', views.cadastrocurso, name='curso'),
]
