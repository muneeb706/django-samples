from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords

class HistoricModel(models.Model):
    history = HistoricalRecords(inherit=True)
    class Meta:
        abstract = True

class TestA(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TestB(HistoricModel):
    name = models.CharField(max_length=200)
    test_a = models.ForeignKey(TestA, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=200, null=True)
    field2 = models.TextField(null=True)
    field3 = models.IntegerField(null=True)
    field4 = models.BooleanField(default=False, null=True)
    field5 = models.DateField(auto_now_add=True, null=True)
    field6 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    field7 = models.EmailField(max_length=254, null=True)
    field8 = models.FileField(upload_to='uploads/', null=True)
    field9 = models.ImageField(upload_to='images/', null=True)
    field10 = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('test_a', 'name',)

class TestC(models.Model):
    id = models.CharField(max_length=200, null=False, primary_key=True)
    test_b = models.ForeignKey(TestB, on_delete=models.CASCADE)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.id