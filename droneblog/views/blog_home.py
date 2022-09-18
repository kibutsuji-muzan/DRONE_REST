from crypt import methods
from droneblog.models.blogs import Blog, RequestBlogger
from droneblog.serializers.blog_serializer import Blogserializer

from droneblog.permissions import IsBlogger

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class PortfolioView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    http_method_names = ['get', 'put', 'post']
    serializer_class = Blogserializer
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.filter(is_active=True)

    def get_serializer_class(self):
        return self.serializer_class


    def get_serializer(self, *args, **kwargs):

        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context(kwargs.get('context'))
        return serializer_class(*args, **kwargs)


    def get_serializer_context(self, context):

        return {
            'context': context,
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    # @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated, IsWorker], url_name='create-blog', url_path='create-blog')
    # def create_blog(self, request):

    #     data = request.data
    #     serializer = self.get_serializer(data=data)

    #     if serializer.is_valid(raise_exception=True):
    #         print(data)
    #         serializer.create(serializer.data)
    #         return Response('portfolio created')

    @action(methods=['post'], detail=False, url_name='update-request', url_path='update-request', permission_classes=['IsAuthenticated'])
    def update_request(self, request):
        try:
            RequestBlogger.objects.get(user=request.user)
        except:
            return Response('Request Already Exist')
        RequestBlogger.objects.create(user=request.user)
        return Response('Request Has Been Sent For Approvel')

    @action(methods=['put'], detail=True, url_name='update-blog', url_path='update-blog', permission_classes=[IsAuthenticated, IsBlogger])
    def update(self, request, pk):
        try:
            instance = Blog.objects.get(id=pk)
        except:
            return Response('Blog Not Exist', status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.update(instance=instance, data=serializer.data)
        return Response('sheesh')


    @action(methods=['post'], detail=False, url_name='create-blog', url_path='create-blog', permission_classes=[IsAuthenticated,IsBlogger])
    def create_blog(self, request):
        data = request.data
        images = request.FILES.getlist('blog_image')
        serializer = self.get_serializer(data=data, context=images)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            data = serializer.data
            serializer.create(data)
        return Response('sheesh')
