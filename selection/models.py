from django.db import models

# Create your models here.

# Model for first dropdown menu, academic subjects
class SubjectDropdown(models.Model):
    subject = models.CharField(max_length=200)
    # Important to make your own __str__ method in each model to see
    # what the actual text is, not just how django represents each object
    SUBJECT_CHOICES = (

    )

    def __str__(self):
        return self.subject

