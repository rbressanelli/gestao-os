from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Client
from .serializers import ClientSerializer


class ClientView(APIView):
    
    def get(self, _) -> Response:        
        client = Client.objects.all()        
        serializer = ClientSerializer(client, many=True)        
        return Response(serializer.data)

    
    def post(self, request) -> Response:        
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   
        client = serializer.save()     
        serializer = ClientSerializer(client)        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    def patch(self, request, client_id) -> Response:        
        client = Client.objects.get(id=client_id)
        serializer = ClientSerializer(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)         
        serializer.save()               
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def delete(self, _, client_id) -> Response:        
        if client_id:
            Client.objects.get(id=client_id).delete()        
        return Response(status=status.HTTP_204_NO_CONTENT)
