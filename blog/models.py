from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created_date = models.DateField(default=date.today)
    text = RichTextField()


    def __str__(self):
        return self.title
