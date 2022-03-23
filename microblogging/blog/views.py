from django.shortcuts import render

from inertia.views import render_inertia
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import models, serializers


def index(request):
    props = {}

    return render_inertia(
        request, 'Index', props,
    )


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
