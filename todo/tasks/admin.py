from django.contrib import admin

from .models.task import Task
from .models.collection import Collection


class TaskAdmin(admin.ModelAdmin):
    pass


class CollectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(Collection, CollectionAdmin)

# Register your models here.
