from django.db import models

# Create your models here.

class Description(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now=True)
    body=models.TextField()
    #picture=models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    description=models.ForeignKey(Description,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.content
