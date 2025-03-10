"""Модуль, содержащий модель Task."""

from django.db import models


class Task(models.Model):
    """Модель задачи."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        """Возвращает строковое представление задачи."""
        return self.title
