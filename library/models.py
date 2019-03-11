from django.db import models

# Create your models here.



class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2) # 999999.99
    pub_date=models.DateTimeField()  # "2012-12-12"
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
    authors=models.ManyToManyField(to="Author")


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    email=models.CharField(max_length=32)
    ad=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    addr=models.CharField(max_length=32)
    tel=models.IntegerField()
    def __str__(self):
        return self.addr
