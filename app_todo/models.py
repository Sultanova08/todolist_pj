from datetime import timezone

from django.db import models


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)

#
# class ToDo(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.TextField(null=True)
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)
#     user = models.ForeignKey(Register, on_delete=models.CASCADE)
#
