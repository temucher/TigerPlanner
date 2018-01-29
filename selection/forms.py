from django import forms
from .models import SubjectDropdown

# potentially find a way to just have this tuple of tuples linked to a csv file? or a table?
SUBJECTS = (
    ('COMP', 'Computer Science'),
    ('COGS', 'Cognitive Science'),
)

class SubjectForm(forms.ModelForm):
    # subject_choice = forms.CharField(label="Subject:", widget=forms.Select(choices=SUBJECTS))

    class Meta:
        model = SubjectDropdown
        fields = ['subject']

class TimeForm(forms.ModelForm):

    class Meta:
        model = SubjectDropdown
        fields = ['time']