from django.db import models

# Create your models here.
class Registration(models.Model):
    nameStudentOne = models.CharField(max_length=75)
    nameStudentTwo = models.CharField(max_length=75, blank=True)
    nameAdvisorOne = models.CharField(max_length=75)
    nameAdvisorTwo = models.CharField(max_length=75, blank=True)
    nameSchool = models.CharField(max_length=75)
    nameArticle = models.CharField(max_length=75, unique=True)
    article = models.FileField(upload_to='articles/')

    def __str__(self):
      return self.nameArticle 