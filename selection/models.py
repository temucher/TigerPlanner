from django.db import models

# Creating tuple for class subjects

SUBJECTS = (
    ('COMP', 'Computer Science'),
    ('COGS', 'Cognitive Science'),
)
# Model for first dropdown menu, academic subjects
class SubjectDropdown(models.Model):
    subject = models.CharField(max_length=200, choices=SUBJECTS)
    # Important to make your own __str__ method in each model to see
    # what the actual text is, not just how django represents each object
    def __str__(self):
        return self.subject

