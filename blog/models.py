from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)
    name_tag = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='home')
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    attached_file = models.FileField(null=True, blank=True, upload_to="files/")
    url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
#       return reverse('article-detail', args=(str(self.id)))
        return reverse('article-detail', kwargs={'pk':self.pk})

