from django.contrib import admin
from .models import AddTool

@admin.register(AddTool)
class AddToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'price', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
