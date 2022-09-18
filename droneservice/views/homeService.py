from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from droneservice.serializers.service_serializers import ServiceSerializer, CategorySerializer, OrderSerializer
from droneservice.models.category import Category
from droneservice.models.service import Service
from droneservice.models.order import orderedService, customer

from accounts.permissions import IsWorker, IsSameUser

class Index(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):

    http_method_names = ['post','get','delete']
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


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
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @action(methods=['get'], detail=True, url_name='get_category', url_path='get-category')
    def categoryretrive(self, request, pk):

        queryset = Service.objects.filter(category=pk, is_active=True)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


    @action(methods=['get'], detail=False, url_name='search_service', url_path='search-service')
    def searchService(self, request):

        queryset = Service.objects.filter(name__contains = request.query_params.get('search'), is_active=True)

        if queryset is not None:
            print(queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response('Service Not Found')


    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated,IsWorker], url_name='create-service',  url_path='create-service')
    def create_Service(self, request, pk):
        if IsSameUser(user=request.user, pk=pk):
            images = request.FILES.getlist('service_image')
            print(images)
            if ((len(images) < 9) and (len(images) > 2)):
                try:
                    category = Category.objects.get(name=request.data.get('category'))
                except:
                    return Response('Category Is Required')

                data=request.data.copy()

                for a in ['owner','name','title','desc','price','category']:
                    try:
                        data.pop(a)
                    except:
                        pass

                request.data.pop('Service_image')
                request.data.pop('category')

                request.data['category'] = str(category.uuid)
                print(request.data)
                serializer = self.get_serializer(data=request.data, context={'service_images':images,'details': data})

                if serializer.is_valid(raise_exception=True):
                    print(serializer.data)
                    serializer.create(serializer.data)
                    return Response('Your Data Has Been Send For Approvel')
            return Response('More Then 8 And Less Then 3 Images Not Allowed')
        return Response('Key And Token Not Matched')


    @action(methods=['delete'], detail=True, permission_classes=[IsAuthenticated,IsWorker], url_name='delete-service',  url_path='delete-service')
    def delete_Service(self, request, pk):
        try:
            Service = Service.objects.get(uuid=pk)
        except:
            return Response('wrong id')
        if Service:
            Service.is_active=False
            Service.save()
            return Response('Your Deletion Request Has Been Sent')

class Others(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = OrderSerializer
    http_method_names = ['get','post','delete']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.user_profile
        return orderedService.objects.filter(customerId__user=user)
    
    @action(methods=['post'], detail=False, url_name='order-item', url_path='order-item')
    def order_item(self, request):
        data = request.data.getlist('uuid')
        items=[]
        try:
            for id in data:
                items.append(Service.objects.get(uuid=id))
            user = request.user.user_profile
        except:
            return Response('Ordered Item Not Valid')

        cust = customer.objects.create(user=user)

        for item in items:
            orderedService.objects.create(customerId=cust, service=item)

        return Response('Your Order Has Been Placed')