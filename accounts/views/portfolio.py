from crypt import methods
from accounts.models.portfolio import Portfolio, PortfolioPost
from accounts.models.userModel import User
from accounts.serializers.portfolio_serializer import PortfolioSerializer ,WithPostsSerializer, PortfolioPostserializer
from accounts.serializers.profile_serializer import OrganizationType
from accounts.permissions import IsWorker

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class PortfolioView(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    http_method_names = ['get', 'put', 'post', 'delete']
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.filter(is_active=True)

    def get_serializer_class(self):
        if ('create-post' in self.request.path):
            return PortfolioPostserializer
        if self.kwargs.get('pk'):
            return WithPostsSerializer
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

    def retrieve(self, request, pk):
        try:
            instance = Portfolio.objects.get(owner=pk)
        except:
            return Response('something went wrong')
        if instance:
            serializer = self.get_serializer(instance)
            print(serializer.data)
            return Response(serializer.data)


    @action(methods=['post'], detail=False, url_name='create_portfolio', url_path='create-portfolio', permission_classes=[IsWorker, IsAuthenticated])
    def create_portfolio(self, request):
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

    @action(methods=['put'], detail=False, url_name='update_portfolio', url_path='update-portfolio', permission_classes=[IsWorker, IsAuthenticated])
    def update_portfolio(self, request):
        try:
            instance = request.user.user_profile.portfolio
        except:
            return Response('Portfolio Not Exist', status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance=instance, data=serializer.data)
        return Response('sheesh')


    @action(methods=['post'], detail=False, url_name='create_post', url_path='create-post', permission_classes=[IsWorker, IsAuthenticated])
    def create_post(self, request):
        data = request.data
        images = request.FILES.getlist('post_image')
        serializer = self.get_serializer(data=data, context={'images':images})
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            data = serializer.data
            data['portfolio'] = request.user.user_profile.portfolio
            print(data)
            serializer.create(data)
        return Response('sheesh')

    @action(methods=['delete'], detail=True, url_name='delete_post', url_path='delete-post', permission_classes=[IsWorker, IsAuthenticated])
    def delete_post(self,request,pk):
        try:
            post=PortfolioPost.objects.get(uuid=pk)
        except:
            return Response('Post Not Exist', status=status.HTTP_400_BAD_REQUEST)
        post.delete()
        return Response('Post Deleted Successfully')