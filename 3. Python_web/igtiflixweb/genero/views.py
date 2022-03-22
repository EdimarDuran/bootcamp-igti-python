from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models
# Create your views here.


def cadastro(request):
    form = forms.GeneroForm()
    
    if request.method=='POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("ERROR")

    genero_list = models.Genero.objects.order_by('descicao')
    data_dict = {"form":form,'genero_records':genero_list}

    data_dict = {'form': form}
    return render(request,'genero/genero.html', data_dict)

def delete(request,id):
    try:
        models.Genero.objects.filter(id=id).delete()
        form = forms.GeneroForm()
        genero_list = models.Genero.objects.order_by('descicao')
        data_dict = {'form': form}
        return render(request,'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed()

def update(request,id):
    item=models.Genero.objects.get(id=id)
    if request.method == "GET":
        form = forms.GeneroForm(initial={"descicao": item.descicao})
        data.dict = {'form':form}
        return render(request,'genero/genero_upd.html',data_dict)
    else:
        form = forms.GeneroForm(request.Post)
        item.descicao = form.data['descicao']
        item.save()
        