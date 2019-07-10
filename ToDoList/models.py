from django.db import models

class ToDoItem(models.Model):
    Content = models.TextField()
    Completed = models.BooleanField()
    #Data = models.DateField(default = 0)
    #Time = models.TimeField(default = 0)
    Author = models.TextField()
    