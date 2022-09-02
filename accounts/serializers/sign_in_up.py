from rest_framework import serializers
from accounts.models.userModel import User
from django.db.models import Q
from django.contrib.auth import authenticate


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'phone', 'gender', 'birthday', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        try:
            if data['email']:
                return data
        except:
            try:
                if data['phone']:
                    return data
            except:
                pass
            raise serializers.ValidationError("Something Went Wrong")

    def create(self, validated_data):

        user = User(email=validated_data['email'], phone=validated_data['phone'],
                    gender=validated_data['gender'], birthday=validated_data['birthday'])

        user.set_password(validated_data['password'])
        user.save()
        return user


class SignInSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        fields = ['email_or_phone', 'password']
