from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import CollectionForm
from .models import Collection,TypeCollection
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def new_Collection(request):
    if request.method == "GET":
        form = CollectionForm()
        collections = Collection.objects.all()
        context = {'form': form, 'collections': collections }
        return render(request, 'collection/collection.html', context)
    else:
        form = CollectionForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('collections')

@login_required(login_url='login')
def details_Collection(request, id=id):
    collection = get_object_or_404(Collection, id=id)
    context = {'collection': collection }
    return render(request, 'collection/details_collection.html', context)

@login_required(login_url='login')
def update_Collection(request, id=id):
    obj = get_object_or_404(Collection, id=id)
    form = CollectionForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('collections')
    #form = CollectionForm(instance = obj)
    context = {'form': form}
    return render(request, 'collection/Update_collection.html', context)

@login_required(login_url='login')
def delete_Collection(request, id=id):
    collection = get_object_or_404(Collection, id=id)
    print(collection)
    collection.delete()
    return redirect('collections')

@login_required(login_url='login')
def get_AllCollections(request):
    collections = Collection.objects.all()
    context = {'collections': collections}
    return render(request, 'collection/all_collection.html', context)

@login_required(login_url='login')
def get_AllFilm(request):
    films = Collection.objects.filter(Type__title='film')
    print(films)
    context = {'films':films}
    return render(request, 'collection/films.html', context)

@login_required(login_url='login')
def get_AllGame(request):
    games = Collection.objects.filter(Type__title='jeux')
    print(games)
    context = {'games':games}
    return render(request, 'collection/games.html', context)

@login_required(login_url='login')
def get_AllSerie(request):
    series = Collection.objects.filter(Type__title='Serie')
    print(series)
    context = {'series':series}
    return render(request, 'collection/series.html', context)






