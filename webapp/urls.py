from re import search
from django.urls import path
from .views import blogform, signup, signin, about, search, blogpage, home, richeditor

urlpatterns = [
    path("", home, name="home"),
    path("sign-up/", signup, name="sign-up"),
    path("sign-in/", signin, name="sign-in"),
    path("about/", about, name="about"),
    path("search/", search, name="search"),
    path("blogform/", blogform, name="blog-form"),
    path("blogpage/", blogpage, name="blogpage"),
    path("editor/", richeditor, name="editor"),
]
