from django.db import models
import uuid


class Technician(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    specialty = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=256, null=False)
    active = models.BooleanField(default=False)
    hiring_date = models.DateTimeField(null=False)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.specialty} - {self.active}'
