from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from droneshop.serializers.product_serializer import ProductSerializer, CategorySerializer, OrderSerializer
from droneshop.models.category import Category
from droneshop.models.product import Product
from droneshop.models.orders import orderedItem, customer

from accounts.permissions import IsWorker, IsSameUser

def validate_data(data):
    req = []
    for d in data:
        try:
            # pro=d.get('product')
            pro = Product.objects.get(uuid=d.get('product'))
            qua = d.get('quantity')
            addr = d.get('address')
            req.append({'product':pro, 'quantity':qua, 'address':addr})
        except:
            return None
    return req


class Index(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    http_method_names = ['post','get','delete']
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


    def get_serializer_class(self):
        if 'get-category-list' in self.request.path:
            return CategorySerializer
        return self.serializer_class


    def get_serializer(self, *args, **kwargs):
        try:
            (kwargs['context']).update(self.get_serializer_context()) 
        except:
            kwargs['context'] = self.get_serializer_context()
    
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)


    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }


    @action(methods=['get'], detail=False, url_name='get_category_list', url_path='get-category-list')
    def categorylist(self, request):
        queryset = Category.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @action(methods=['get'], detail=True, url_name='get_category', url_path='get-category')
    def categoryretrive(self, request, pk):
        try:
            queryset = Product.objects.filter(category=pk, is_active=True)
        except:
            return Response('not Valid key', status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


    @action(methods=['get'], detail=False, url_name='search_product', url_path='search-product')
    def searchproduct(self, request):
        name = str(request.query_params.get('search'))
        queryset = Product.objects.filter(name__contains = name, is_active=True)

        if queryset is not None:
            print(queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response('Product Not Found')


    @action(methods=['post'], detail=False, permission_classes=[IsAuthenticated,IsWorker], url_name='create_product',  url_path='create-product')
    def create_product(self, request):
        images = request.FILES.getlist('product_image')
        print(images)
        if ((len(images) < 9) and (len(images) > 2)):
            try:
                category = Category.objects.get(name=request.data.get('category'))
                try:
                    request.data.pop('product_image')
                except:
                    return Response('images required')
            except:
                return Response('Category Is Required')

            data=request.data.copy()
            for a in ['name','title','desc','price','category']:
                try:
                    data.pop(a)
                except:
                    pass

            request.data.pop('category')
            request.data['category'] = str(category.uuid)
            request.data['owner'] = request.user.user_profile
            print(request.data)
            serializer = self.get_serializer(data=request.data, context={'product_images':images,'details': data})
            if serializer.is_valid(raise_exception=True):
                print(serializer.data)
                serializer.create(serializer.data)
                return Response({'response':'Your Data Has Been Send For Approvel','data':serializer.data})
        return Response({'response':'More Then 8 And Less Then 3 Images Not Allowed'})


    @action(methods=['delete'], detail=True, permission_classes=[IsAuthenticated,IsWorker], url_name='delete_product',  url_path='delete-product')
    def delete_product(self, request, pk):
        try:
            product = Product.objects.get(uuid=pk)
        except:
            return Response('wrong id')
        if product:
            product.is_active=False
            product.save()
            return Response('Your Deletion Request Has Been Sent')

class Others(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    serializer_class = OrderSerializer
    http_method_names = ['get','post','delete']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.user_profile
        return orderedItem.objects.filter(customerId__user=user)


    def get_serializer(self, *args, **kwargs):
        try:
            (kwargs['context']).update(self.get_serializer_context()) 
        except:
            kwargs['context'] = self.get_serializer_context()
    
        serializer_class = self.serializer_class
        return serializer_class(*args, **kwargs)


    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    @action(methods=['post'], detail=False, url_name='order-item', url_path='order-item')
    def order_item(self, request):

        serializer = OrderSerializer(data=request.data, many=True)
        cust = customer.objects.create(user=request.user.user_profile)

        if serializer.is_valid(raise_exception=True):
            res = validate_data(data=request.data)
            print(res)
            if res is not None:
                for items in res:
                    orderedItem.objects.create(customerId=cust,**items)
                return Response('Your Order Has Been Placed')
            return Response('Your given data is not valid', status=status.HTTP_400_BAD_REQUEST)
