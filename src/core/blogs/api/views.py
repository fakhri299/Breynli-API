from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView,ListAPIView
from blogs.models import *
from blogs.api.serializers import *
from.qs import *

class CategoryApiView(ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()


class BlogApiView(ListAPIView):
    serializer_class=BlogSerializer
    queryset=blog_list()



class BlogDetailApiView(RetrieveAPIView):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()