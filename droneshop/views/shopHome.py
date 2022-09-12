from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from droneshop.models.product import Product
from droneshop.serializers.Serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class Index(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SellersPage(APIView):

    def get(self, request, slug):

        query = Product.objects.filter(product_uuid=slug)
        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data)
