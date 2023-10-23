from django.db import models

# Create your models here.


from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    age = models.FloatField()


    def __str__(self):
        return self.sName
    

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)


    def __str__(self):
        return self.title