from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class NoteForm(models.Model):
    title = models.CharField(max_length=150)
    note = models.TextField()
    cat = models.OneToOneField(Category,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title 