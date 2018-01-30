from django.shortcuts import render
from .models import ClassData
from .forms import SubjectForm # , TimeForm, ISGNForm
from django.views.generic import FormView, CreateView

# may end up needing a new view for a results page?

def home(request):
    # template_name = 'select_class.html'
    subject_form = SubjectForm()
    # time_form = TimeForm()
    # isgn_form = ISGNForm()
    return render(request, 'selection/home.html', {'subject_form': subject_form})

                                                   # 'time_form': time_form,
                                                   # 'isgn_form': isgn_form})

# dont think this is needed
'''
class CreateSubjectDropdown(CreateView):
    model = ClassData
    form_class = SubjectForm
    template_name = 'selection/home.html'
'''