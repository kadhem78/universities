from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import University , Student
from django.views.generic import ListView



# Create your views here.
class UniversityListView(ListView):
    model = University
    template_name = "university_list.html"
    context_object_name = 'universities'

class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"

    def get_queryset(self):
        self.university = get_object_or_404(University , slug = self.kwargs['slug'])
        return Student.objects.filter(university = self.university)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["university"] = self.university
        return context
    
    



