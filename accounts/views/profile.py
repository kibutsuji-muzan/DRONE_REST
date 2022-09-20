from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import mixins

from django.db.models import Q

from accounts.models.profileModel import UserProfile
from accounts.models.userModel import UpdateRequest, OrganizationType
from accounts.serializers.profile_serializer import ProfileSerializer, RequestUpdateSerializer, OrganizationTypeSerializer
from accounts.permissions import *
from accounts.permissions import IsSameUser



class Profile(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    http_method_names = ['get', 'put', 'post']
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()


    def get_serializer_class(self):
        if 'update-request' in self.request.path:
            return RequestUpdateSerializer
        if 'get-org-types' in self.request.path:
            return OrganizationTypeSerializer
        return ProfileSerializer


    def get_serializer(self, *args, **kwargs):
        try:
            (kwargs['context']).update(self.get_serializer_context()) 
        except:
            kwargs['context'] = self.get_serializer_context()

        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)


    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

        return context

    def update(self, request, pk):
        if IsSameUser(user=request.user, pk=pk):
            instance = request.user
            data = {}
            profile_image = request.FILES.get('profile_image')
            print(profile_image)
            print(len(request.data))
            if len(request.data) < 7:
                return Response('All Fields Must Be Sent To Update Profile',status.HTTP_400_BAD_REQUEST)
            if len(request.data) > 7:
                return Response('More Than Enough Fields Were Sent',status.HTTP_400_BAD_REQUEST)
            print(request.data)
            for field in request.data:
                data[field] = request.data.get(field)
            data['profile_image'] = {'image':profile_image}
            print(data)
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.update(instance=instance, data=data)
            return Response('Your Account Detail Has Been Updated',status.HTTP_200_OK)
        return Response('id and token not matched')


    @action(methods=['post'], detail=False, url_name='update-request', url_path='update-request', permission_classes=[IsAuthenticated])
    def update_request(self, request):
        
        data={}
        for key,value in request.data.items():
            data[key]=value

        try:
            if UpdateRequest.objects.get(user=request.user):
                return Response('Request Already Exist')
        except:
            pass
        try:
            org=OrganizationType.objects.get(type=(str(data.get('org')).lower()))
        except:
            return Response('org Not Valid')
        print(data)
        data.pop('org')
        data['org']=org
        serializer = self.get_serializer(data=data, context={'org':org})
        if serializer.is_valid(raise_exception=True):
            serializer.create(data=serializer.data)
            #Add Send Email Or Phone Signal
            return Response('Your Request Is Sent Wait For Approvel')

        return Response(status=status.HTTP_400_BAD_REQUEST)