from django.shortcuts import render

from inertia.views import render_inertia


def index(request):
    props = {}

    return render_inertia(
        request, 'Index', props,
    )
