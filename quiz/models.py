from django.db import models

# Create your models here.
class Quiz(models.Model):

    class Meta:
        verbose_name_plural = "Quiz"

    quiz_name = models.CharField(max_length=254)

    def __str__(self):
        return self.quiz_name

class Questions(models.Model):

    class Meta:
        verbose_name_plural = "Questions"

    quiz = models.ForeignKey(
            'Quiz', null=False, blank=False, on_delete=models.CASCADE,
            related_name='questions')
    question = models.CharField(max_length=254)
    first_answer = models.CharField(max_length=254)
    second_answer = models.CharField(max_length=254)
    third_answer = models.CharField(max_length=254)
    fourth_answer = models.CharField(max_length=254)
    answer = models.CharField(max_length=254)

    def __str__(self):
        return self.quiz.quiz_name
