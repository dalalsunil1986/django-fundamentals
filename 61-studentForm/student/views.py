from django.shortcuts import render
from . import models, forms

def Register(request):
    return render(request=request, template_name='register.html', context={
        'form': forms.StudentForm(),
    })
