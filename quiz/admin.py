from django.contrib import admin
from .models import Quiz, Questions, Results
# Register your models here.


class QuizAdmin(admin.ModelAdmin):
    # Admin display
    list_display = (
        'id',
        'quiz_name',
    )
    # Ordering in admin
    ordering = ('id',)

class QuestionsAdmin(admin.ModelAdmin):
    # Admin display
    list_display = (
        'question',
    )
    # Ordering in admin
    ordering = ('id',)

class ResultsAdmin(admin.ModelAdmin):
    # Admin display
    list_display = (
        'staff',
        'quiz_name',
    )
    # Ordering in admin
    ordering = ('id',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Results, ResultsAdmin)

