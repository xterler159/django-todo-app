from django.db import models
import uuid


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE)
