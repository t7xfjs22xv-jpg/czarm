from django.db import models

class FreedomPost(models.Model):
    # We add a name field that defaults to Anonymous if left blank
    name = models.CharField(max_length=100, default="Anonymous", blank=True)
    content = models.TextField()
    bible_verse = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)