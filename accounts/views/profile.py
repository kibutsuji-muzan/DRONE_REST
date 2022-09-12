from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import mixins

from django.db.models import Q

from accounts.models.profileModel import UserProfile
from accounts.serializers.profile_serializer import ProfileSerializer



class Profile(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    http_method_names = ['get', 'put']
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    @action(methods=['put'], detail=False, url_name='update_profile', url_path='update-profile')
    def update_profile(self, request):
        instance = UserProfile.objects.get(user=request.user)
        data = {}
        profile_image = request.FILES.get('profile_image')
        print(len(request.data))

        if len(request.data) < 7:
            return Response('All Fields Must Be Sent To Update Profile',status.HTTP_400_BAD_REQUEST)
        if len(request.data) > 7:
            return Response('More Than Enough Fields Were Sent',status.HTTP_400_BAD_REQUEST)
        
        for field in request.data:
            data[field] = request.data.get(field)

        data['profile_image'] = {'image':profile_image}
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.update(instance=instance, data=data)

        return Response('Your Account Detail Has Been Updated',status.HTTP_200_OK)