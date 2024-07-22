from django.contrib.auth import  login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import LoginSerializer
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .models import StsUser
from .serializers import StsUserSerializer, AdminSerializer, CustomerSerializer
from rest_framework.authtoken.models import Token
import random
import string
from django.core.mail import EmailMessage 
from django.conf import settings
import threading
from django.contrib.sites.shortcuts import get_current_site




accounts = ''.join(random.choices('0123456789', k=4))
Alphabet =list(string.ascii_uppercase)
A = random.choice(Alphabet)
B = random.choice(Alphabet)
C = random.choice(Alphabet)
accountNum = f'{A}{B}{C}{accounts}'
code = accountNum

print(code)


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_code(user,request):
    current_site = get_current_site(request).domain
    email_subject =  "Activate Your Secure Ticketing Solution Account"
    email_body =  f"""
                        Welcome to the Secure Ticketing Solution, {user.full_name}!

                        Thank you for registering with our secure ticketing solution. To activate your account and start managing your tickets, please enter the following activation code:

                        {code}

                        Once activated, you can log in using the following credentials:

                        Username or Email
                    
                        Important Security Note:

                        * Please do not share your activation code or login credentials with anyone.
                        * We will never ask you for your password via email.
                        * Once logged in, navigate to the "Settings" section to view your username
                        * If you have any difficulty activating your account, please contact support at support.sts@gmail.com.

                        We look forward to helping you manage your tickets securely!

                        Sincerely,

                        The Secure Ticketing Solution Team
                        """
    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[user.email]
                         )
    
    EmailThread(email).start()
    

class ActivateAccountAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        activation_code = request.data.get('code').lower()
        if not activation_code:
            return Response({'error': 'Activation code is required.'}, status=status.HTTP_400_BAD_REQUEST)
        user = StsUser.objects.filter(code=activation_code, is_active=False).first()
        if not user:
            user = StsUser.objects.filter(code=activation_code, is_active=True).first()
            if not user:
                return Response({'error': 'Invalid activation code.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message' : 'activated.'}, status=status.HTTP_200_OK)
        else:
            user.is_active = True
            user.save()
            return Response({'message': 'Account activated successfully.'}, status=status.HTTP_200_OK)
   

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        account_type = user.account_type  
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'success',
            'account_type': account_type,
            'token': token.key 
        }, status=status.HTTP_200_OK)



class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            print(user.token) 
            print('Printing token')
            user.token = None 
            user.save()  
            print('Token deleted successfully')
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f'Error: {e}')  
            return Response({"error": "An error occurred."}, status=status.HTTP_400_BAD_REQUEST)


class UserManagementViewSet(viewsets.ModelViewSet):
    queryset = StsUser.objects.all() 
    serializer_class = StsUserSerializer  
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        account_type = self.request.data.get('account_type', None)
        if account_type == 'bussiness':
            print('here bussiness')
            return AdminSerializer
        elif account_type == 'personal':
            print('personal')
            return CustomerSerializer
        else:
            return StsUserSerializer

    def perform_create(self, serializer):
        full_name = serializer.validated_data['full_name']
        num = random.randint(0, 1000)
        num_str = str(num)
        username = full_name.split()[0].lower() +num_str+'@sts'
        user=serializer.save(username=username)
        user.set_password(serializer.validated_data['password'])
        user.code = code.lower()
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        send_code(user, self.request)
        print(token.key)
        return user, token.key

    def create(self, request, *args, **kwargs):
        data = request.data
        password = data.get('password')
        password2 = data.get('password2')
        account_type = data.get('account_type')
        print(password)
        print(password2)
        if account_type == 'bussiness':
            national_id = data.get('national_id')
            if not national_id:
                return Response({'national_id': 'National Id is  required for business accounts.'})
        if password != password2:
            return Response({'password2': ['Passwords do not match']}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)