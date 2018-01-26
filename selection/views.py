from django.shortcuts import render
from .models import SubjectDropdown
from .forms import SubjectForm
from django.views.generic import FormView, CreateView


def home(request):
    # template_name = 'select_class.html'

    return render(request, 'selection/home.html')

class CreateSubjectDropdown(CreateView):
    model = SubjectDropdown
    form_class = SubjectForm
    template_name = 'selection/home.html'