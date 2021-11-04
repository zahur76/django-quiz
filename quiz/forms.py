from django import forms
from .models import Quiz, Questions


class add_quizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'quiz_name': 'Quiz Name',
        }

        self.fields['quiz_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs[
                'placeholder'] = placeholders[field]
            self.fields[field].widget.attrs[
            'class'] = 'border-dark m-1 rounded-0 mx-auto add_quiz-form-input'
            self.fields[field].label = False

class add_questionForm(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ('quiz',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'question': 'question',
            'first_answer': 'first_answer',
            'second_answer': 'second_answer',
            'third_answer': 'third_answer',
            'fourth_answer': 'fourth_answer',
            'answer': 'answer',
        }

        self.fields['question'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs[
                'placeholder'] = placeholders[field]
            self.fields[field].widget.attrs[
            'class'] = 'border-dark m-1 rounded-0 mx-auto add_quiz-form-input'
            self.fields[field].label = False
