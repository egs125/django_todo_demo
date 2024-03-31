from django.db import models

class Todo(models.Model):
  todo_content = models.CharField(max_length=500)
  is_done = models.BooleanField(default=False)
  def __str__(self):
    return self.todo_content
