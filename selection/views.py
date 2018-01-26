from django.shortcuts import render
from .models import SubjectDropdown
from .forms import SubjectForm
from django.views.generic import FormView, CreateView

# may end up needing a new view for a results page?

def home(request):
    # template_name = 'select_class.html'
    form = SubjectForm()
    return render(request, 'selection/home.html', {'form': form})

class CreateSubjectDropdown(CreateView):
    model = SubjectDropdown
    form_class = SubjectForm
    template_name = 'selection/home.html'