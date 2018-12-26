from django.contrib import admin
from core.models import Answer


# Register your models here.
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'university', 'created_at']
    ordering = ['-created_at']
