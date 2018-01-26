from django import forms
from .models import SubjectDropdown

SUBJECTS = (
    ('COMP', 'Computer Science'),
    ('COGS', 'Cognitive Science'),
)

class SubjectForm(forms.Form):
    # subject_choice = forms.CharField(lable="Subject:", widget=forms.Select(choices=SUBJECTS))

    class Meta:
        model = SubjectDropdown
        fields = ['subject']