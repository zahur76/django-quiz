from django import forms

from .models import Staff


class add_staffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "employee_number": "Employee Number",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email_address": "Email Address",
        }

        self.fields["employee_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = placeholders[field]
            self.fields[field].widget.attrs[
                "class"
            ] = "border-dark m-1 rounded-0 mx-auto add_staff-form-input"
            self.fields[field].label = False
