from django.urls import path
from blogs.api.views import *

urlpatterns = [
    
    path('blogs/',BlogApiView.as_view()),
    path('blogs/<int:pk>',BlogDetailApiView.as_view()),

    path('categories',CategoryApiView.as_view()),
    
    path('contact',ContactApiView.as_view()),

    path('consultacy',ConsultantApiView.as_view())

]
