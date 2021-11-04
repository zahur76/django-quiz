from django.db import models

# Create your models here.
class Quiz(models.Model):

    class Meta:
        verbose_name_plural = "Quiz"

    quiz_name = models.CharField(max_length=254)

    def __str__(self):
        return self.quiz_name
