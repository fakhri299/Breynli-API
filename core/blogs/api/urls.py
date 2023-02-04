from django.urls import path
from blogs.api.views import *

urlpatterns = [
    
    path('',BlogApiView.as_view()),
    path('<int:pk>',BlogDetailApiView.as_view()),

    path('categories',CategoryApiView.as_view()),
    
    path('contact',ContactApiView.as_view()),

    path('consultant',ConsultantApiView.as_view())

]
