from django.db import models
import uuid


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=256, unique=True, null=False)
    telephone = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

