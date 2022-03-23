from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name="index"),
    path('publications', views.publications, name="publications"),
    path('create/publication', views.create_publication, name="create_publication"),
]
