from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32, null=False)
    description = models.TextField(max_length=512)
    
    service_order = models.ForeignKey(
        "service_orders.ServiceOrder", on_delete=models.CASCADE, related_name="service_orders"
    )
    
    
    def __str__(self):
        return self.name

