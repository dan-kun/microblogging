from django.shortcuts import render, redirect

from inertia.views import render_inertia
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import models, serializers
from marshmallow import ValidationError
from django.http import JsonResponse


def index(request):
    return redirect("blog:publications")


def publications(request):
    # Get all publications and ordering by votes_rate
    pub_obj = models.Publication.objects.all()
    pub_list = list(pub_obj)
    pub_list.sort(key=lambda pub: pub.votes_rate)

    # Paginate the publications
    paginate_by = 10
    page = request.GET.get("page")
    paginator = Paginator(pub_list, paginate_by)
    try:
        pub_pages = paginator.page(page)
    except PageNotAnInteger:
        pub_pages = paginator.page(1)
    except EmptyPage:
        pub_pages = paginator.page(paginator.num_pages)

    # Schema for publications
    pub_schema = serializers.PublicationsSchema(many=True)
    publications_json = pub_schema.dump(pub_pages)

    props = {
        "count": pub_obj.count(),
        "paginateBy": paginate_by,
        "pages": paginator.num_pages,
        "currentPage": int(page) if page else 1,
        "publications": publications_json,
    }

    return render_inertia(
        request,
        "Publications",
        props,
    )


def create_publication(request):
    if request.method == "POST":
        pub_schema = serializers.CreatePublicationSchema()
        try:
            data = pub_schema.loads(request.body)
        except ValidationError as err:
            raise ValueError("Error en data")
        else:
            publication = models.Publication(
                title=data.get("title"),
                author=data.get("author"),
                content=data.get("content")
            )
            publication.save()

    return redirect("blog:publications")


def publication_details(request, publication_id):
    try:
        pub = models.Publication.objects.get(id=publication_id)
    except models.Publication.DoesNotExist:
        raise ValueError("Esta publicación no existe")

    pub_schema = serializers.PublicationsSchema()
    publication = pub_schema.dump(pub)

    props = {
        "publication": publication
    }

    return render_inertia(
        request,
        "PublicationDetails",
        props
    )


def edit_publication(request, publication_id):
    if request.method == "POST":
        try:
            publication = models.Publication.objects.get(id=publication_id)
        except models.Publication.DoesNotExist:
            raise ValueError("Esta publicación no existe")

        pub_schema = serializers.CreatePublicationSchema()
        try:
            data = pub_schema.loads(request.body)
        except ValidationError as err:
            raise ValueError("Error en data")
        else:
            publication.title = data.get("title")
            publication.author = data.get("author")
            publication.content = data.get("content")
            publication.save()

            return redirect("blog:publication_details", publication_id)

    return redirect("blog:publications")


def delete_publication(request, publication_id):
    try:
        publication = models.Publication.objects.get(id=publication_id)
    except models.Publication.DoesNotExist:
        raise ValueError("Esta publicación no existe")

    publication.delete()

    return redirect("blog:publications")


def vote_system(request, publication_id, vote_type):
    if vote_type.lower() not in ["up", "down"]:
        return JsonResponse(
            {
                "success": False,
                "message": "Tipo de votación no habilitada"
            },
            status=400, safe=True
        )
    try:
        publication = models.Publication.objects.get(id=publication_id)
    except models.Publication.DoesNotExist:
        return JsonResponse(
            {
                "success": False,
                "message": "Esta publicación no existe"
            },
            status=400, safe=True
        )

    if vote_type.lower() == "up":
        publication.up_votes += 1
    else:
        publication.down_votes += 1
    publication.save()

    return JsonResponse({"success": True}, status=200, safe=True)
