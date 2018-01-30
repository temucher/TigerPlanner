from django import forms
from .models import ClassData

# potentially find a way to just have this tuple of tuples linked to a csv file? or a table?
# also don't think this needs to be here
SUBJECTS = (
    ('COMP', 'Computer Science'),
    ('COGS', 'Cognitive Science'),
)

class SubjectForm(forms.ModelForm):
    # subject_choice = forms.CharField(label="Subject:", widget=forms.Select(choices=SUBJECTS))

    class Meta:
        model = ClassData
        fields = ['subject', 'time', 'isgn']


'''
class TimeForm(forms.ModelForm):

    class Meta:
        model = ClassData
        fields = ['time']

class ISGNForm(forms.ModelForm):

    class Meta:
        model = ClassData
        fields = ['isgn']
'''

