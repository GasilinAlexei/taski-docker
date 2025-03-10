"""Модуль настройки административной панели Django."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Административная настройка модели Task."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
