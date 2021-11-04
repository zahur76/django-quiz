from django.contrib import admin
from .models import Quiz
# Register your models here.


class QuizAdmin(admin.ModelAdmin):
    # Admin display
    list_display = (
        'id',
        'quiz_name',
    )
    # Ordering in admin
    ordering = ('id',)

admin.site.register(Quiz, QuizAdmin)
