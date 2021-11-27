from django.db import models
from staff.models import Staff
# Create your models here.
class Quiz(models.Model):

    class Meta:
        verbose_name_plural = "Quiz"

    quiz_name = models.CharField(max_length=254)
    pass_mark = models.IntegerField(default=75)

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

class Results(models.Model):

    class Meta:
        verbose_name_plural = "Results"

    staff= models.ForeignKey(
            'staff.Staff', null=False, blank=False, on_delete=models.CASCADE,
            related_name='results')
    quiz_name = models.CharField(max_length=254)
    results = models.CharField(max_length=254)
    attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    pass_fail = models.CharField(max_length=254)

    def __str__(self):
        return self.staff.first_name
