from accounts.serializers.sign_in_up import SignUpSerializer, SignInSerializer
from accounts.serializers.user_profile import UserSerializer
from accounts.models.userModel import User
from core.settings import REST_KNOX as knox_settings

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.serializers import DateTimeField
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from knox.models import AuthToken

from django.contrib.auth.signals import user_logged_in
from django.utils import timezone
from django.db.models import Q

class SignUpInView(ModelViewSet):

    http_method_names= ['post']
    serializer_class = SignUpSerializer

    def get_context(self):
        return {'request': self.request, 'format': self.format_kwarg, 'view': self}

    def get_token_ttl(self):
        return knox_settings['TOKEN_TTL']

    def get_token_limit_per_user(self):
        return knox_settings['TOKEN_LIMIT_PER_USER']

    def get_expiry_datetime_format(self):
        return knox_settings['EXPIRY_DATETIME_FORMAT']

    def format_expiry_datetime(self, expiry):
        datetime_format = self.get_expiry_datetime_format()
        return DateTimeField(format=datetime_format).to_representation(expiry)

    def get_post_response_data(self, request, token, instance, user):
        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        if request is not None:
            if UserSerializer is not None:
                data["user"] = UserSerializer(user,context=self.get_context()).data
        else:
            if UserSerializer is not None:
                data["user"] = UserSerializer(user).data

        return data

    @action(methods=['post'], detail=False,url_name='signup',url_path='signup')
    def signup(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # print(serializer.data)

            data = serializer.data
            user = serializer.create(data=data)
            token_ttl = self.get_token_ttl()
            instance, token = AuthToken.objects.create(user, token_ttl)
            print(instance)
            print(token)
            data = self.get_post_response_data(token=token,instance=instance,user=user,request=None)
            # user_logged_in.send(sender=request.user.__class__,request=request, user=request.user)
            return Response(data)
        return Response({'status': 400})

    @action(methods=['post'], detail=False,url_name='signin',url_path='signin')
    def signin(self, request, format=None):
        print(request.user)

        token_limit_per_user = self.get_token_limit_per_user()
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            data = serializer.data
            user = User.objects.get(Q(email=data['email_or_phone']) or Q(phone=data['email_or_phone']))
            print(user)

            if token_limit_per_user is not None:
                now = timezone.now()
                token = request.user.auth_token_set.filter(expiry__gt=now)
                if token.count() >= token_limit_per_user:
                    return Response(
                        {"error": "Maximum amount of tokens allowed per user exceeded."},
                        status=status.HTTP_403_FORBIDDEN
                    )

            token_ttl = self.get_token_ttl()
            instance, token = AuthToken.objects.create(user, token_ttl)
            print(instance, token)
            # user_logged_in.send(sender=request.user.__class__,request=request, user=request.user)
            data = self.get_post_response_data(request=request,token=token,instance=instance,user=user)

            return Response(data)
        
