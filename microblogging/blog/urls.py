from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name="index"),
    path('publications', views.publications, name="publications"),
    path('create/publication', views.create_publication, name="create_publication"),
    path('publication/<str:publication_id>',
         views.publication_details, name="publication_details"),
    path('publication/edit/<str:publication_id>',
         views.edit_publication, name="edit_publication"),
    path('publication/delete/<str:publication_id>',
         views.delete_publication, name="delete_publication"),
    path('publication/votes/<str:publication_id>/<str:vote_type>',
         views.vote_system, name="vote_system"),
]
