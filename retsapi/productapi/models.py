from django.db import models

# Create your models here.


class Product (models.Model):
    name = models.CharField(max_length=100)
    description= models.CharField(max_length=500)
    age=models.IntegerField()
    email_id=models.EmailField()
    time=models.DateTimeField(auto_now_add=10)
    #picture=models.ImageField(upload_to='pictures/y/m/d',max_length=255,null=True, blank=True)


    def __str__(self):
        return"{0} and {1}".format(self.name,self.email_id)