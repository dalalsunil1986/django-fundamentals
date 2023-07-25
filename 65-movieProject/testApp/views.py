from django.shortcuts import render, redirect
from . import models, forms

from django.views.generic import ListView

class MovieListView(ListView):
    model = models.Movie 
    template_name = 'index.html'

def addMovieView(request):
    form = forms.MovieForm()

    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('all_movies')
    
    return render(request, template_name='add_movie.html', context={
        'form': form,
    })
