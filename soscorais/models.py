from django.db import models

# Create your models here.
class registration(models.Model):
    nameStudentOne = models.CharField(max_length=255)
    nameStudentTwo = models.CharField(max_length=255, blank=True)
    nameAdvisorOne = models.CharField(max_length=255)
    nameAdvisorTwo = models.CharField(max_length=255, blank=True)
    nameSchool = models.CharField(max_length=255)
    nameArticle = models.CharField(max_length=255)
    article = models.FileField(upload_to='articles/')

    def __str__(self):
      return self.nameArticle 