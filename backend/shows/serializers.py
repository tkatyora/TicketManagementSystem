from rest_framework.serializers import ModelSerializer
from .models import Show
from rest_framework import serializers






class ShowSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False)
    showDate = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    created_on = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"], read_only=True)
    updated_on = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"], read_only=True)
    class Meta:
        model = Show
        fields = '__all__'
        read_only_fields = ('created_on', 'updated_on')