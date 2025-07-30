from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_active')
    search_fields = ('title', 'location', 'description')
    list_filter = ('is_active', 'date')
    
    
    ordering = ('date',)
    list_editable = ('is_active',)
    list_per_page = 10
    
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'description')
        }),
        ('Деталі події', {
            'fields': ('date', 'location', 'is_active')
        }),
    )
        
    
admin.site.register(Event, EventAdmin)