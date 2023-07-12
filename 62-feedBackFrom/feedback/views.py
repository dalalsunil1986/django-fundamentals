from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect


def feedbackView(request):
    form = forms.FeedBackForm()

    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        roll = request.POST['rollno']
        print(roll)
        if form.is_valid():
            name = form.cleaned_data
            print(name, '----')
            return HttpResponseRedirect('/feedback/')

    return render(request=request, template_name='index.html', context={
        'forms': form,
    })

