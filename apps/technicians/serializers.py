from rest_framework import serializers
from .models import Technician


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'
    
    
    def create(self, validated_data):
        return Technician.objects.create(**validated_data)
    
    def update(self, instance: Technician, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name) 
        instance.last_name = validated_data.get("last_name", instance.last_name) 
        instance.specialty = validated_data.get("specialty", instance.specialty)
        instance.email = validated_data.get("email", instance.email)
        instance.hiring_date = validated_data.get("hiring_date", instance.hiring_date)        
        instance.save()
        return instance


class TecnicianActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model: Technician
        fields = ['active']
    
    
    def update(self, instance: Technician, validated_data):
        instance.save()
        return instance
