from django.shortcuts import render
from django.views.generic import TemplateView
from program.models import UserProgram
from course.models import Course

# Create your views here.
# class PriceView(TemplateView):
#     template_name='pricing.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["program_list"] = UserProgram.objects.all()
#         print(context)
#         print(context["program_list"])
#         return context


def PriceView(request):
    courses = Course.objects.all()
    for course in courses:
        print(course)
    context = {
        'courses': courses,
    }
    return render(request, 'pricing.html', context)
