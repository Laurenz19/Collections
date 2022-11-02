from django.db import models
from django.urls import reverse

# Create your models here.

class TypeCollection(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title

class Collection(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    producer = models.CharField(max_length=250, blank=False, null=False)
    Type = models.ForeignKey(TypeCollection, on_delete=models.CASCADE)
    datepublish = models.DateField()
    description = models.TextField(blank=False, null=False)
    photo = models.ImageField(null=True, blank=True)

    def getUrl_forUpdate(self):
        return reverse("update_collection", kwargs={"id": self.id})#f"/collection/update/{self.id}/"
    
    def getUrl_forDetails(self):
        return reverse("details_collection", kwargs={"id": self.id})#f"/collection/{self.id}/"
    
    def getUrl_forDelete(self):
        return reverse("delete_collection", kwargs={"id":self.id})
    
    def __int__(self):
        return self.id
    
    def __str__(self):
        return self.name


    



