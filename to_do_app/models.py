from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField()
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title