from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 300)
    logo = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 300)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(on_delete = models.CASCADE)
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    url = models.URLField(max_length = 500,blank = True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageFiled(upload_to = 'media')
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.name
