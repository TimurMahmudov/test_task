from django import template

from categories.models import Category

register = template.Library()


@register.filter
def active(url, request):
    return (url == request.get_full_path())


@register.inclusion_tag("include/active_cat.html")
def enclosure_menu(cat_id=None):
    cats_menu = {
        "cat_id": cat_id
    }
    if cat_id is None:
        cats_menu["super_cats"] = Category.objects.filter(super_category=None)
        return cats_menu
    cat = Category.objects.select_related(
        "super_category",
        "super_category__super_category"
    ).prefetch_related("subs").get(pk=cat_id)
    cats_menu["cat"] = cat
    cats_menu["subs"] = cat.subs.all()
    if cat.super_category is None:
        cats_menu["super_cats"] = Category.objects.filter(super_category=None)
    else:
        super_id = cat.super_category.super_category
        cats_menu["super_cats"] = Category.objects.filter(
            super_category=super_id
        )
    return cats_menu
