from rest_framework.views import APIView
from accounts.models.userModel import User
from accounts.serializers.sign_in_up import SignUpSerializer

class SignupView(APIView):

    def post(self, request):

        data = request.data
        serializer = SignUpSerializer(data=data)
        
