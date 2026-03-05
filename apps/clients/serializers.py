from rest_framework import serializers
from .models import Client
from ..service_orders.serializers import ServiceOrderSerializer


class ClientSerializer(serializers.ModelSerializer):
    
    service_order = ServiceOrderSerializer(required=False)
    
    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "email", "telephone", "address", "created_at", "service_order"]
        
        
    def create(self, validated_data):
        return Client.objects.create(**validated_data)    

        
    def update(self, instance: Client, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name) 
        instance.last_name = validated_data.get("last_name", instance.last_name) 
        instance.email = validated_data.get("email", instance.email) 
        instance.telephone = validated_data.get("telephone", instance.telephone)
        instance.address = validated_data.get("address", instance.address) 
        instance.save()
        return instance
    