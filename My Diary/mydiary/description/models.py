from django.db import models

# Create your models here.

class Description(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    #picture=models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
