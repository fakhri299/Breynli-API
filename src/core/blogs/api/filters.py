from django_filters import FilterSet
from blogs.models import Blog,Category


class BlogFilter(FilterSet):
    class Meta:
        model=Blog
        fields={
            
        'category':['exact'], 
        
        }

