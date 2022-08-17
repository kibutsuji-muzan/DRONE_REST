from rest_framework.response import Response
from rest_framework.views import APIView
from drone_api.models.product import Product
from drone_api.serializers.productSerializer import ProductSerializer

# query database get objects then serialize that query to json and send response to url 127.0.0.1/api

class TestView(APIView):
    
    def get(self, request):
        query = Product.objects.all()
        print(query.select_related)
        serializer = ProductSerializer(query,many=True)
        print(serializer.data)
        return Response(serializer.data) #sending response