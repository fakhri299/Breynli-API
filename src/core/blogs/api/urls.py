from django.urls import path
from blogs.api.views import *

urlpatterns = [
    path('categories',CategoryApiView.as_view()),
    path('',BlogApiView.as_view()),
    path('<int:pk>',BlogDetailApiView.as_view())
]
