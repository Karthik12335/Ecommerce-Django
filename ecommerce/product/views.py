from django.db import connection
from drf_spectacular.utils import extend_schema
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from sqlparse import format

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryView(viewsets.ViewSet):
    """
    A simple view set for viewing all category
    """

    queryset = Category.objects.all().isactive()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    """
    A simple view set for viewing all Brand
    """

    queryset = Brand.objects.all().isactive()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    """
    A simple view set for viewing all Product
    """

    queryset = Product.objects.all().isactive()
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug)
            .select_related("category", "brand")
            .prefetch_related("product_line__product_image"),
            many=True,
        )
        data = Response(serializer.data)
        q = list(connection.queries)
        print(len(q))
        for qs in q:
            sqlfromatted = format(str(qs["sql"]), reindent=True)
            print(highlight(sqlfromatted, SqlLexer(), TerminalFormatter()))
        return data
        # return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    @action(
        methods=["get"], detail=False, url_path=r"category/(?P<category>[\w-]+)/all"
    )
    def list_product_by_category(self, request, category=None):
        """
        An endpoint to view products by category
        """
        serializer = ProductSerializer(
            self.queryset.filter(category__name=category), many=True
        )
        return Response(serializer.data)
