from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255,default="")
    body=models.TextField(default="")
    url = models.TextField(default="")
    icon= models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    pub_date= models.DateTimeField(default="")
    
    
    
    votes_total= models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]