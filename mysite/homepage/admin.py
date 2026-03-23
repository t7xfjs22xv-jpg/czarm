from django.contrib import admin
from .models import FreedomPost

@admin.register(FreedomPost)
class FreedomPostAdmin(admin.ModelAdmin):
    # This shows these columns in the admin dashboard list
    list_display = ('name', 'content', 'bible_verse', 'created_at')
    
    # Adds a sidebar to filter by date
    list_filter = ('created_at',)
    
    # Adds a search bar for names and post text
    search_fields = ('name', 'content')