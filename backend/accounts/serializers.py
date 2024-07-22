from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import StsUser, Admin, Customer

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})
    
    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get('password')

        if username_or_email and password:

            try:
                user = User.objects.get(Q(email=username_or_email) | Q(username=username_or_email))
            except User.DoesNotExist:
                raise serializers.ValidationError({'error': 'Invalid username or email.'})

            if not user.check_password(password):
                raise serializers.ValidationError({'error': 'Incorrect password.'})
            if not user.is_active:
                raise serializers.ValidationError({'error': 'Please activate your account.'})
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError({'error': 'Email and password are required.'})


class StsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StsUser
        fields = '__all__'



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    # def validate(self, attrs):
    #     account_type = attrs.get('account_type')
    #     if account_type == 'bussiness':
    #         national_id = attrs.get('national_id')
    #         if not national_id:
    #             raise serializers.ValidationError({'national_id': 'National Id is  required for business accounts.'})
        
    #     return attrs

    # def create(self, validated_data):
    #     return Admin.objects.create_user(**validated_data
    #     )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
