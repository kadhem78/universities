from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class University(models.Model):
    name = models.CharField(max_length=150) 
    slug = models.SlugField(null = True , blank = True)
    country = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

    def save(self , *args, **kwargs) : 
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE , related_name = "students")
    full_name = models.CharField(max_length=150) 
    field = models.CharField(max_length=150) 
    graduate_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.full_name
    