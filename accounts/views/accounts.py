from accounts.serializers.accounts_serializer import SignUpSerializer, SignInSerializer, PasswordResetSerializer
from accounts.serializers.profile_serializer import UserSerializer
from accounts.models.userModel import User, PassResetToken
from accounts.models.userOtp import VerificationDevice
from accounts.signals import Send_Mail, Send_Sms
from core import settings


from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import DateTimeField
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from rest_framework.reverse import reverse

from knox.models import AuthToken
from post_office.models import EmailTemplate
from phonenumbers import parse as validate_phone
from pyisemail import is_email as validate_email

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q

class Base:
    def get_context(self):
        return {'request': self.request, 'format': self.format_kwarg, 'view': self}

    def get_token_ttl(self):
        return settings.REST_KNOX['TOKEN_TTL']

    def get_token_limit_per_user(self):
        return settings.REST_KNOX['TOKEN_LIMIT_PER_USER']

    def get_expiry_datetime_format(self):
        return settings.REST_KNOX['EXPIRY_DATETIME_FORMAT']

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
                data["user"] = UserSerializer(user, context=self.get_context()).data
        else:
            if UserSerializer is not None:
                data["user"] = UserSerializer(user).data

        return data

    def valid_email_phone(self, email_or_phone):
        try:
            email = validate_email(address=email_or_phone, check_dns=True)
        except:
            return None
        if email:
            return {'email': True, 'phone': False}
        try:
            if validate_phone(email_or_phone):
                return {'phone': True, 'email': False}
        except:
            return None

    def createtoken(self, user):
        token = PassResetToken.objects.create(user=user)
        return token

    def get_user(self,pk):
        try:
            user = User.objects.get(id=pk)
        except:
            return None
        return user

    def get_otp(self, user):
        totp = user.verification_device
        otp = totp.generate_challenge()
        return otp


class OTPManagement:

    @action(methods=['get'], detail=True, url_name='get_otp', url_path='get-otp')
    def getotp(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except:
            return Response('User With This Key Not Exist')
        if not user.is_active:
            otp = self.get_otp(user)

            smsdata = {
            'message' : f'Hi There Your Otp is {otp}',
            }
            context = {
                'otp': otp
            }
            maildata = {
                'mail':EmailTemplate.objects.get(name='get-otp'),
                'context':{
                    'otp':otp
                }
            }
            response = {
                'response':'Your Otp Has Been Sent To Your Phone',
                'verify-otp-url':reverse('accounts-otp_verification', kwargs={'pk':user.id}, request=request)
            }
            if user.email:

                Send_Mail.send(sender=user, data=maildata)
                print(otp)
                return Response(response)

            if user.phone:
                Send_Sms.send(sender=user, data=smsdata)
                print(otp)
                return Response(response)
        return Response('Your Account Is Already Verified')


    @action(methods=['post'], detail=True, url_name='otp_verification', url_path='otp-verification')
    def verify_otp(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            if user.is_active:
                return Response('User Already Verified')
        except:
            return Response('User With This Key Not Exist')
        totp = user.verification_device
        otp = request.data.get('otp')
        res={
            'resend-otp':reverse('accounts-get_otp', kwargs={'pk':pk}, request=request)
        }
        res['response']='OTP is Required'
        if otp is not None:
            res['response']='OTP is incorrect'
            if totp.verify_token(otp):
                res={
                    'signin-url':reverse('accounts-signin', request=request)
                }
                user.is_active = True
                user.save()
                user.refresh_from_db
                return Response(res)
            return Response(res, status.HTTP_400_BAD_REQUEST)
        return Response(res)

class PasswordManagement:

    @action(methods=['post'], detail=False, url_name='get_reset_link', url_path='get-reset-link')
    def get_reset_link(self, request):
        email_or_phone = self.valid_email_phone(request.data.get('email_or_phone'))
        if email_or_phone is not None:
            try:
                user = User.objects.get(Q(email=request.data.get('email_or_phone')) if email_or_phone.get('email') else Q(phone=request.data.get('email_or_phone')))
            except:
                return Response('User With This Token Does Not Exist', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Email Or Phone Not Valid', status=status.HTTP_400_BAD_REQUEST)

        token = PassResetToken.objects.filter(user=user)

        if token:
            token.delete()
            token = self.createtoken(user=user)
        else:
            token = self.createtoken(user=user)

        reset_link = reverse('accounts-pass_reset',kwargs={'pk':token.token}, request=request)
        print(reset_link)
        maildata = {
            'mail':EmailTemplate.objects.get(name='get-reset-link'),
            'context':{
                'reset_link':reset_link
            }
        }

        smsdata = {
            'message' : f'Hi There Your Reset Link is {reset_link}',
            }

        if email_or_phone.get('email'):
            Send_Mail.send(sender=user, data=maildata)
            print(token.token)
            return Response('Reset Link Has Been Sent To Your Email')

        if email_or_phone.get('phone'):
            Send_Sms.send(sender=user, data=smsdata)
            print(smsdata)
            return Response('Reset Link Has Been Sent To Your Phone Number')
        return Response('Something Went Wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(methods=['post'], detail=True, url_name='pass_reset', url_path='pass-reset')
    def password_reset(self, request, pk):
        try:
            token = PassResetToken.objects.get(token=pk)
        except:
            return Response('Your Token Is Expired Or Incorrect', status=status.HTTP_400_BAD_REQUEST)
        serializer = PasswordResetSerializer(data=request.data, context={'user': token.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'response':'Your Password Has Been Reset', 'signin-url':reverse('accounts-signin',request=request)})
        return Response('Something Went Wrong', status=status.HTTP_500_INTERNAL_SERVER_ERROR)




#Master Class Used In Urls
class AccountsManagement(Base, OTPManagement, PasswordManagement, viewsets.GenericViewSet):

    http_method_names = ['post','get','delete']
    serializer_class = SignUpSerializer

    @action(methods=['post'], detail=False, url_name='signup', url_path='signup')
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('im in')
            data = serializer.data
            user = serializer.create(data=data)
            if user:
                data = {
                    'User': serializer.data.get('email_or_phone'),
                    'response': 'Registration Succesfull',
                    'get-otp-url': reverse('accounts-get_otp', kwargs={'pk':user.id}, request=request)
                }
                return Response(data)
        return Response({'status': 400})


    @action(methods=['post'], detail=False, url_name='signin', url_path='signin')
    def signin(self, request, format=None):

        token_limit_per_user = self.get_token_limit_per_user()
        serializer = SignInSerializer(data=request.data, context={'TTL':token_limit_per_user})

        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            try:
                user = User.objects.get(phone=data['email_or_phone'])
            except:
                user = User.objects.get(email=data['email_or_phone'])

            if not user.is_active:
                return Response(f'id: {user.id}')

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
            data = self.get_post_response_data(request=request, token=token, instance=instance, user=user)
            print(data)
            return Response(data)


    @action(methods=['delete'], detail=False, url_name='delete_user', url_path='delete-user', permission_classes=[IsAuthenticated,])
    def delete_user(self, request):
        try:
            user = User.objects.get(user = request.user)
        except:
            return Response('User With This Token Does Not Exist', status=status.HTTP_400_BAD_REQUEST)
        if (request.user == user):
            data = request.data.get('password')
            if user.check_password(data):
                user.delete()
                return Response('Your Account Has Been Deleted')

            return Response('Password Is Incorrect', status=status.HTTP_400_BAD_REQUEST)
        return Response('Your User Token Or Auth Token Are Not Same', status=status.HTTP_400_BAD_REQUEST)

