from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from droneshop.serializers.category_serializer import CategorySerializer
from droneshop.serializers.product_serializer import ProductSerializer
from droneshop.models.category import Category
from droneshop.models.product import Product

class Index(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    http_method_names = ['post','get']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_serializer_class(self):
        if self.request.method == 'GET':
            if 'get-category-list' in self.request.path:
                return CategorySerializer
            return self.serializer_class


    def get_serializer(self, *args, **kwargs):

        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context(kwargs.get('context'))
        return serializer_class(*args, **kwargs)


    def get_serializer_context(self, context):
        """
        Extra context provided to the serializer class.
        """
        return {
            'context': context,
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }


    @action(methods=['get'], detail=False, url_name='get_category_list', url_path='get-category-list')
    def categorylist(self, request):
        queryset = Category.objects.all()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_name='get_category', url_path='get-category')
    def categoryretrive(self, request, pk):

        queryset = Product.objects.filter(category=pk)
        serializer = self.get_serializer(queryset)

        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_name='search_product', url_path='search-product')
    def searchproduct(self, request):

        queryset = Product.objects.filter(name__contains = request.query_params.get('search'))
            
        if queryset is not None:
            print(queryset)
            serializer = self.get_serializer(queryset, many=True)

            return Response(serializer.data)
        return Response('Product Not Found')