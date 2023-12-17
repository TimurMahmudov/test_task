from django.urls import path

from .views import category_posts, index

app_name = "menu"


urlpatterns = [
    path("", index, name="index"),
    path("categories/<int:cat_id>/", category_posts, name="category"),
]
