from django.shortcuts import get_object_or_404, render

from .models import Category


def index(request):
    context = {"cat_id": None}
    return render(request, "index.html", context)


def category_posts(request, cat_id):
    cat = Category.objects.get(pk=cat_id)
    context = {
        "cat": cat,
        "cat_id": cat_id
    }
    template_name = "category.html"
    return render(request, template_name, context)
