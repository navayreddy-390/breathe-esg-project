from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)

class DataSource(models.Model):
    source_name = models.CharField(max_length=100)

class EmissionRecord(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    original_value = models.FloatField()
    normalized_value = models.FloatField()
    unit = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="pending")
