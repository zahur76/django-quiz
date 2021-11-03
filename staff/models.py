from django.db import models

# Create your models here.
class Staff(models.Model):

    class Meta:
        verbose_name_plural = "Staff"

    employee_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name
