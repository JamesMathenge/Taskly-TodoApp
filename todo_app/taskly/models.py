from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if self.due_date and self.due_date < timezone.now():
            raise ValidationError("Due date cannot be in the past.")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "To-Do"
        verbose_name_plural = "To-Dos"
        indexes = [
            models.Index(fields=['due_date']),  
        ]



