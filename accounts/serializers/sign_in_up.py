from rest_framework import serializers

from django.db.models import Q
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from accounts.models.userModel import User

import re
from email_validator import validate_email
from phonenumbers import parse as validate_phone


class SignUpSerializer(serializers.ModelSerializer):
    email_or_phone = serializers.CharField()

    class Meta:
        model = User
        fields = ['email_or_phone', 'gender', 'birthday', 'password']

    def validate(self, data):
        try:
            if User.object.get(Q(email=data['email_or_phone']) and Q(phone=data['phone'])):
                print('e a p')
                error = 'both exist'
        except:
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

        if error == 'both exist':
            raise serializers.ValidationError(
                'User with This Email And Phone Already Exist')

        if error == 'email':
            raise serializers.ValidationError(
                'User with This Email Already Exist')

        if error == 'phone':
            raise serializers.ValidationError(
                'User with This phone Already Exist')

    def valid_email_phone(self, email_or_phone):
        try:
            email = validate_email(email_or_phone).email
            if email:
                return {'email': email, 'phone': False}
        except:
            try:
                if validate_phone(email_or_phone, None):
                    return {'phone': email_or_phone, 'email': False}
            except:
                raise serializers.ValidationError('Not Valid')

    def create(self, data):
        email_or_phone = self.valid_email_phone(
            email_or_phone=data['email_or_phone'])
        print(email_or_phone)
        errors = []
        try:
            validate_password(data['password'])
            if email_or_phone['email']:
                user = User.objects.create(
                    email=email_or_phone['email'], birthday=data['birthday'], gender=data['gender'])
                return user
            else:
                user = User.objects.create(
                    phone=email_or_phone['phone'], birthday=data['birthday'], gender=data['gender'])
                return user
        except ValidationError as e:
            for error in e:
                print(error)
                errors.append(str(error))
            raise serializers.ValidationError(errors)


class SignInSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = ['email_or_phone', 'password']

    def valid_email_phone(self, email_or_phone):
        try:
            email = validate_email(email_or_phone).email
            if email:
                return {'email': email, 'phone': False}
        except:
            try:
                if validate_phone(email_or_phone, None):
                    return {'phone': email_or_phone, 'email': False}
            except:
                raise serializers.ValidationError('Not Valid')

    def validate(self, data):
        if self.valid_email_phone(data['email_or_phone']):
            try:
                user = User.objects.get(
                    Q(email=data['email_or_phone']) or Q(phone=data['email_or_phone']))
                if user:
                    return data
            except:
                raise serializers.ValidationError(
                    'User With This Email Or Phone Not Found')
        else:
            raise serializers.ValidationError(
                'User With This Email Or Phone Not Found')

    def authenticate(self, email_or_phone=None, password=None):
        try:
            user = User.objects.get(
                Q(email=email_or_phone) | Q(phone=email_or_phone))
            print('i am in')
        except:
            pass
        if user.check_password(password) and user.is_active:
            print(password)
            print(user)
            if authenticate(user):
                return user
            else:
                raise serializers.ValidationError(
                    'User With This Email Or Phone Not Found')
        else:
            raise serializers.ValidationError(
                'Password For This User Is Incorrect')
