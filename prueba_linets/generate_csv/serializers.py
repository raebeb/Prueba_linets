from rest_framework import serializers
from .models import MasterProductsConfigurable

class MasterProductsConfigurableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProductsConfigurable
        fields = '__all__'