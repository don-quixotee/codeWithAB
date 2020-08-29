from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = [('D',"Draft"), ("P","published")]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    status = models.CharField(max_length = 50, choices=STATUS, default='D')
    image = models.ImageField(upload_to='post')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    auther = models.CharField(max_length=50)
    def __str__(self):
        return self.content




    