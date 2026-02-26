from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Technician
from .serializers import TechnicianSerializer


class TechnicianView(APIView):
    def get(self, _) -> Response:
        technicians = Technician.objects.all()
        serializer = TechnicianSerializer(technicians, many=True)
        return Response(serializer.data)
    
    
    def post(self, request) -> Response:
        serializer = TechnicianSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        technician = serializer.save()
        serializer = TechnicianSerializer(technician)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def patch(self, request, technician_id) -> Response:
        technician = Technician.objects.get(id=technician_id)
        serializer = TechnicianSerializer(technician, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
    
    def delete(self, _, technician_id) -> Response:
        if technician_id:
            Technician.objects.get(id=technician_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
