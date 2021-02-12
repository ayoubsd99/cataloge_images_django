from django.db import models

# Create your models here.


class Image(models.Model):
    image=models.TextField()
    title=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey("catalog.Category",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    label=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.label

        