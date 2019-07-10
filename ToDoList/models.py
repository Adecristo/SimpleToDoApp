from django.db import models

class ToDoItem(models.Model):
    Content = models.TextField()
    Completed = models.BooleanField()
    Author = models.TextField()
    #todo:
    #Data = models.DateField(default = 0)
    #Time = models.TimeField(default = 0)
    def __str__(self):
        return self.Content