from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    title=models.CharField(max_length=200)
    url = models.TextField(max_length=200)
    body = models.TextField(max_length=200)
    upvote_total=models.IntegerField(default=1)
    image=models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    pub_date=models.DateTimeField()
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)

    def date(self):
        return self.pub_date.strftime('%b %e,%y')

    def summary(self):
        return self.body[0:10]
    def __str__(self):
        return self.title




# Create your models here.
