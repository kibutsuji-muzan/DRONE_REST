from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from django.db.models import Q

from accounts.models.profileModel import UserProfile
from accounts.serializers.user_profile import ProfileSerializer

class EnablePartialUpdateMixin:
    """Enable partial updates

    Override partial kwargs in UpdateModelMixin class
    https://github.com/encode/django-rest-framework/blob/91916a4db14cd6a06aca13fb9a46fc667f6c0682/rest_framework/mixins.py#L64
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class Profile(ModelViewSet, EnablePartialUpdateMixin):

    http_method_names = ['get', 'patch', 'put']
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()

# def update(self, request, pk=None):
    #     print(request.data)
    #     print(pk)
    #     return Response('Working...')

    # def partial_update(self, request, pk=None):
    #     print(request.data)
    #     print(pk)
    #     return Response('Working')

    def list(self, request):
        return Response('Method \"GET\" not allowed.')

    @action(methods=['patch'], detail=True, url_name='update_profile_pic', url_path='update-profile-pic')
    def update_profile_pic(self, request, pk):
        print(pk)
        try:
            profile_pic = request.FILES.get('profile_image')
            try:
                profile = UserProfile.objects.get(user = request.user)
            except:
                return Response(status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Hello..')
        print(profile_pic)
        print(profile)
        print(request.data)
        return Response(status.HTTP_400_BAD_REQUEST)