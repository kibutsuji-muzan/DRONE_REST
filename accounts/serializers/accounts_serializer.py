from urllib import request
from rest_framework import serializers

from django.db.models import Q
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from accounts.models.userModel import User

import re
from phonenumbers import parse as validate_phone
from pyisemail import is_email as validate_email


class SignUpSerializer(serializers.ModelSerializer):
    email_or_phone = serializers.CharField()

    class Meta:
        model = User
        fields = ['email_or_phone', 'password']

    def validate(self, data):
        try:
            print(data['email_or_phone'])
            if User.objects.get(phone=data['email_or_phone']):
                print('p')
                error = 'phone'
        except:
            try:
                if User.objects.get(email=data['email_or_phone']):
                    print('e')
                    error = 'email'
            except:
                return data

        if error == 'email':
            raise serializers.ValidationError(
                'User with This Email Already Exist')

        if error == 'phone':
            raise serializers.ValidationError(
                'User with This phone Already Exist')

    def valid_email_phone(self, email_or_phone):
        email = validate_email(address=email_or_phone, check_dns=True)
        if email:
            return {'email': email_or_phone, 'phone': False}
        try:
            if validate_phone(email_or_phone):
                return {'phone': email_or_phone, 'email': False}
        except:
            raise serializers.ValidationError('Not Valid')

    def create(self, data):
        email_or_phone = self.valid_email_phone(email_or_phone=data.get('email_or_phone'))
        print(email_or_phone)
        errors = []
        try:
            if validate_password(data.get('password')) is None:
                print('password is valid')
                if email_or_phone.get('email'):
                    user = User.objects.create(email=email_or_phone.get('email'))
                    user.set_password(data.get('password'))
                    user.is_active = False
                    user.save()
                    return user
                else:
                    user = User.objects.create(phone=email_or_phone.get('phone'))
                    user.set_password(data.get('password'))
                    user.is_active = False
                    user.save()
                    return user
        except ValidationError as e:
            print('password not valid or other exception')
            for error in e:
                print(error)
                errors.append(str(error))
            raise serializers.ValidationError(errors)


class SignInSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = ['email_or_phone', 'password']

    def valid_user(self, email_or_phone):
        try:
            user = User.objects.get(email=email_or_phone)
        except:
            try:
                user = User.objects.get(phone=email_or_phone)
            except:
                raise serializers.ValidationError('User With This Email Or Phone Not Exsist')


        if user:
            print(user)
            return user

    def authenticate(self ,password, user):
        print('im in')
        if user.check_password(password):
            return True
        else:
            raise serializers.ValidationError('Password For This User Is Incorrect')

    def validate(self, data):
        user = self.valid_user(data.get('email_or_phone'))
        print(user)
        if user and user.is_active:
            print('im in')
            auth = self.authenticate(password=data.get('password'), user=user)
            if auth:
                print(user)
                return data
        raise serializers.ValidationError('User Is Not Active')

class PasswordResetSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['password1', 'password2']

    def validate(self, data):
        errors=[]
        if data.get('password1') == data.get('password2'):
            try:
                if validate_password(data.get('password1')) is None:
                    user = self.get_serializer_context.get('user')
                    user.set_password(data.get('password1'))
                    user.save()
                    user.refresh_from_db
                    return data
            except ValidationError as e:
                for error in e:
                    print(error)
                    errors.append(str(error))
                raise serializers.ValidationError(errors)
        raise serializers.ValidationError('Passwords Must Be Same')