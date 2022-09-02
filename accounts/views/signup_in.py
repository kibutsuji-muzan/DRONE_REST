from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers.sign_in_up import SignUpSerializer, SignInSerializer#, phone_SignInSerializer
from accounts.models.userModel import User
from django.db.models import Q

class SignUp(APIView):

    def post(self, request):
        try:
            user=request.user
        except:
            pass

        data = request.data
        serializer = SignUpSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            # serializer.create(serializer.data)

        return Response(serializer.data)

class SignIn(APIView):

    def get_user(self):

        return self.request.user

    def authenticate(self,email_or_phone=None, password=None):
        try:
            user = User.objects.get(Q(email=email_or_phone)|Q(phone=email_or_phone))
            # pwd = user.password
            print('i am in')
            c = user.check_password(password)
            if c and user.is_active:
                print(password)
                print(user)
                return user
        except:
            pass

    def post(self,request):

        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            user = self.authenticate(**serializer.data)
            if user:
                print(user)

        return Response(serializer.data)
