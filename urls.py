from django.urls import path
from .views import blog_list
from .models import blog
urlpatterns = [
    path('',blog_list)
]