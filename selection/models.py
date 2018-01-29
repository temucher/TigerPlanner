from django.db import models

# Creating tuple for class subjects

SUBJECTS = (
    ('COMP', 'Computer Science'),
    ('COGS', 'Cognitive Science'),
)

TIMES = (
    ('9:35 - 10:30', '9:35 - 10:30'),
    ('default', 'default')
)
# Model for first dropdown menu, academic subjects
# RENAME, make this one model for all class data
# Started doing that by adding a time field
class SubjectDropdown(models.Model):
    subject = models.CharField(max_length=200, choices=SUBJECTS)
    time = models.CharField(max_length=200, choices=TIMES, default='DEFAULT_VALUE')
    # Important to make your own __str__ method in each model to see
    # what the actual text is, not just how django represents each object
    def __str__(self):
        return self.subject

