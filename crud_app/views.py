from django.shortcuts import render
from django.shortcuts import redirect

from crud_app.forms import FilmForm
from crud_app.models import Film


def create(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/read')
            except: 
                pass
    else:
        form = FilmForm()
    return render(request,'index.html',{'form':form})

def read(request):
    fid = request.GET.get('id')

    if fid is not None:
        films = [Film.objects.get(id=fid)]
    else:
        n = request.GET.get('n')

        films = list(Film.objects.all())

        if n is not None:
            n = int(n)
            if n < len(films) and n > 0:
                films = films[-n:]

    return render(request,"show.html",{'films':films})

def update(request, id):
    film = Film.objects.get(id=id)

    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect("/read")

        for field in form:
            print("Field Error:", field.name,  field.errors)
    else:
        form = FilmForm()

    return render(request,'edit.html', {'film':film, 'form': form})

def delete(request, id):
    film = Film.objects.get(id=id)

    film.delete()
    return redirect("/read")
