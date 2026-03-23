from django.contrib import admin
from django.urls import path
from homepage.views import wall_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wall_view, name='wall'),
]