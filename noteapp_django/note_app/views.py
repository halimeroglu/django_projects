from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from .models import *
from .forms import *
# Create your views here.
def index(request):
    post = NoteForm.objects.all()

    if (request.GET.get('DeleteButton')):
        NoteForm.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('/')

    if request.method == 'POST':
        form = NoteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = NoteForms()       
    context = {
        'post':post,
        'form': form,
    }
    return render(request,'index.html',context)

class Index_Detail(DetailView):
    template_name = 'index_detail.html'
    queryset = NoteForm.objects.all()


def cat(request):
    post = Category.objects.all()

    if (request.GET.get('DeleteButton')):
        Category.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('category')

    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    form = CatForm()        
    context = {
        'post':post,
        'form':form,
    }
    return render(request,'category.html',context)