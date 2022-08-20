from django.db import models

# Create your models here.


class AddClass(models.Model):
    id=models.AutoField(primary_key=True)
    class_title=models.CharField(max_length=30)
    total_seat=models.IntegerField()
    available_seat=models.IntegerField()
    def __str__(self):
        return self.class_title+"-"+str(self.total_seat)+"-"+str(self.available_seat)








