from django.contrib import admin
from administrators.models import Administrator

# Register your models here.
class Administrators(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')
    list_display_links = ('id', 'username')
    ordering = ('username',)
    search_fields = ('username',)
    list_per_page = 10

admin.site.register(Administrator, Administrators)