from django.db import models

# Create your models here.
class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=20)