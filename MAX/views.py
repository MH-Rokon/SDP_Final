from django.shortcuts import render, redirect
from  doctor.models import Doctor, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from accounts  import forms, models


from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'
def home(request):
    data = Doctor.objects.all()
    return render(request, 'home2.html', {'data': data})
def pa(request):
   
    return render(request, 'pa.html')

@login_required
def book(request):
    data = Doctor.objects.all()
    return render(request, 'home.html', {'data': data})

@login_required
def it(request):
    category_instance = Category.objects.get(name='Heart')  
    data = Doctor.objects.filter(categories=category_instance)
    return render(request, 'it.html', {'data': data})

@login_required
def tragedy(request):
    category_instance = Category.objects.get(name='Medicine')  
    data = Doctor.objects.filter(categories=category_instance)
    return render(request, 'tragedy.html', {'data': data})

@login_required
def drama(request):
    category_instance = Category.objects.get(name='Child') 
    data =  Doctor.objects.filter(categories=category_instance)
    return render(request, 'drama.html', {'data': data})

@login_required
def all(request):
    data =  Doctor.objects.all()
    return render(request, 'all.html', {'data': data})

@login_required
def add_book(request, id):
    book = models.Book.objects.get(pk=id) 
    book_form = forms.BookForm(instance=book)
    if request.method == 'POST': 
        book_form = forms.BookForm(request.POST, instance=book)
        if book_form.is_valid(): 
            book_form.instance.author = request.user
            book_form.save() 
            return redirect('profile') 
    
    return render(request, 'add_book.html', {'form': book_form})

