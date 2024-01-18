from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse_lazy
from . import forms
from . import models
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from doctor.models import Doctor,Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.shortcuts import render, redirect
from .models import Profile

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Doctor
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Doctor
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Doctor
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class DetailPostView(DetailView):
    model = models.Doctor
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
 
    

@login_required
def buy(request, id):
    post = models.Car.objects.get(pk=id) 
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST': 
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid(): 
            post_form.instance.author = request.user
            post_form.save() 
            return redirect('buy') 
    
    return render(request, 'buy.html', {'form' : post_form})