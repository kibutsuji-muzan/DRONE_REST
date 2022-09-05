from accounts.models.userModel import User
from accounts.models.profileModel import UserProfile, ProfileUpdateRequest, ProfileImage, ProfileType

from rest_framework import serializers
from email_validator import validate_email
from phonenumbers import parse as validate_phone


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', ]


class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileImage
        fields = ['image', 'alt_txt', 'id']


class ProfileSerializer(serializers.ModelSerializer):

    profile_image = ProfileImageSerializer(read_only=False)

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'phone', 'first_name',
                  'last_name', 'gender', 'birthday', 'profile_image']

    def email_valid(self, email):
        try:
            if validate_email(email, None).email:
                return email
        except:
            raise serializers.ValidationError('Email Not Valid')

    def phone_valid(self, phone):
        try:
            if validate_phone(phone, None):
                return phone
        except:
            raise serializers.ValidationError('Phone Number Not Valid')

    def validate_email(self, email):
        email = self.email_valid(email)
        try:
            user = User.objects.get(email=email)
            if user:
                raise serializers.ValidationError('This Email Already Exists')
        except:
            return email

    def validate_phone(self, phone):
        phone = self.phone_valid(phone)
        try:
            user = User.objects.get(phone=phone)
            if user:
                raise serializers.ValidationError('This Phone Number Already Exists')
        except:
            return phone

    def update(self, instance, data):
        print(instance)
        print(data)
        return instance