from django.contrib import admin
from soscorais.models import Registration

# Register your models here.
class Registrations(admin.ModelAdmin):
    list_display = ('id', 'nameStudentOne', 'nameStudentTwo', 'nameAdvisorOne', 'nameAdvisorTwo', 'nameSchool', 'nameArticle', 'article')
    list_display_links = ('id', 'nameArticle')
    ordering = ('nameArticle',)
    search_fields = ('nameStudentOne', 'nameStudentTwo', 'nameAdvisorOne', 'nameAdvisorTwo', 'nameSchool', 'nameArticle',)
    list_per_page = 10

admin.site.register(Registration, Registrations)