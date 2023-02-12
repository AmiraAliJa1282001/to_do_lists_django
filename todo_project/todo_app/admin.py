from django.contrib import admin

# Register your models here.

from todo_app.models import ToDoItem, ToDoList
admin.site.register(ToDoItem)
admin.site.register(ToDoList)