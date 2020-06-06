from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=120)
    profile_img = models.ImageField()
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=120)
    food_type = models.ManyToManyField('Genre')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    img = models.ImageField()
    

    def __str__(self):
        return self.title
