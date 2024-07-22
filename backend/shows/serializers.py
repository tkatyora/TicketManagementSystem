from rest_framework.serializers import ModelSerializer
from .models import Show
from rest_framework import serializers



class  ShowSerializer(ModelSerializer):
    picture = serializers.ImageField(required=False)
    class Meta:
        model = Show
        fields = '__all__'
        read_only_fields = ('created_on', 'updated_on')

  