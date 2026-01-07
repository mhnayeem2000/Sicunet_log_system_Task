from django.db import models

# Create your models here.

class AccessLog(models.Model):
    card_id = models.CharField(max_length=100)
    door_name = models.CharField(max_length=100)
    access_granted = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.timestamp}  card: {self.card_id}   Door: {self.door_name}   granted: {self.access_granted}"
    
