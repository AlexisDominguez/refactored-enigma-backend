from django.db import models
from app.notebooks.models import Notebooks


class Notes(models.Model):
    content = models.CharField(max_length=19999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notebook = models.ForeignKey(Notebooks, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.content
