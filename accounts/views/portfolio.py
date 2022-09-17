from crypt import methods
from accounts.models.portfolio import Portfolio
from accounts.models.userModel import User
from accounts.serializers.portfolio_serializer import PortfolioSerializer ,WithPostsSerializer, PortfolioPostserializer
from accounts.serializers.profile_serializer import ShopOrganizationType
from accounts.permissions import IsWorker, IsSameUser

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class PortfolioView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    http_method_names = ['get', 'put', 'post']
    serializer_class = PortfolioSerializer
    permission_classes = [IsWorker, IsAuthenticated]

    def get_serializer_class(self):
        if (self.request.method=='GET'):
            return WithPostsSerializer
        if 'create-post' in self.request.path:
            return PortfolioPostserializer
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


    def retrieve(self, request, pk):
        try:
            instance = Portfolio.objects.get(owner=pk)
        except:
            return Response('something went wrong')
        if instance:
            serializer = self.get_serializer(instance)
            print(serializer.data)
            return Response(serializer.data)



    def create(self, request):
        try:
            request.user.user_profile.portfolio
            return Response('Portfolio Already Exists', status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        data = request.data 
        serializer = self.get_serializer(data=data)

        if serializer.is_valid(raise_exception=True):
            print(data)
            serializer.create(serializer.data)
            return Response('portfolio created')


    def update(self, request, pk):
        if IsSameUser(user = request.user, pk=pk):
            try:
                instance = request.user.user_profile.portfolio
            except:
                return Response('Portfolio Not Exist', status=status.HTTP_400_BAD_REQUEST)

            data = request.data
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.update(instance=instance, data=serializer.data)
            return Response('sheesh')
        return Response('id and token not matched')


    @action(methods=['post'], detail=True, url_name='create-post', url_path='create-post')
    def create_post(self, request, pk):
        if IsSameUser(user = request.user, pk=pk):
            data = request.data
            images = request.FILES.getlist('post_image')
            serializer = self.get_serializer(data=data, context=images)
            if serializer.is_valid(raise_exception=True):
                print(serializer.data)
                data = serializer.data
                data['portfolio'] = request.user.user_profile.portfolio
                print(data)
                serializer.create(data)
            return Response('sheesh')
        return Response('id and token not matched')
