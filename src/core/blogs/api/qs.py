from django.db.models.query import QuerySet
from blogs.models import Blog, Category

def blog_list() -> QuerySet[Blog]:
    qs = Blog.objects.select_related('category', 'author').all()
    return qs

def category_list() -> QuerySet[Category]:
    qs = Category.objects.all()
    return qs