from django.db import models

# Create your models here.

class Assignments(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    added_at=models.DateTimeField(auto_now_add=True)
    submission_date=models.DateField()

class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    subject=models.CharField(max_length=100)
    added_date=models.DateTimeField(auto_now_add=True)

