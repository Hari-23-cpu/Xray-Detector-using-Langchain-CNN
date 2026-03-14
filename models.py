from django.db import models

class Scan(models.Model):
    patient_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='scans/')
    ai_report = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scan for {self.patient_name} - {self.created_at}"
