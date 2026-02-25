from django.db import models
import uuid


class ServiceOrder(models.Model):
    
    PRIORITY_CHOICES = (
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta')
    )
    
    STATUS_CHOICES = (
        ('opened', 'Aberta'),
        ('in_progress', 'Em andamento'),
        ('concluded', 'Concluída'),
        ('canceled', 'Cancelada')
    )
    
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    os_number = models.CharField(max_length=20, null=False)
    problem_description = models.TextField(max_length=1024, null=False)
    status = models.CharField(choices=STATUS_CHOICES, default='opened')
    priority = models.CharField(choices=PRIORITY_CHOICES, default='low')
    created_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateTimeField(null=False)
    
    
    def __str__(self):
        return f'{{"OS": {self.os_number}, "Prioridade": {self.priority},"Status": {self.status},"Descrição": {self.problem_description}}}'

