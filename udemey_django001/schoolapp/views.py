from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from . import forms as fm
from  schoolapp.models import Teacher


## my notes
##  TemplateView    -> direct link to a normal html file  eg thankyou.html ie no imput expected
##  FormView        -> direct link to a form html (no database involved) where an input is expected eg contact.html
##  CreateView(ModelForm)   ->    



def homeview(request):
    # note this this is the previous way
    return render(request, "schoolapp/homefunction.html") 


class HomeView(TemplateView):
    # note this this is the new way using templates instead of functions
    template_name="schoolapp/homeclass.html"

    pass

class Thanks(TemplateView):
    template_name="schoolapp/thankyou.html"

class ContactForm(FormView):
    # note need to also crrate forms.py 
    form_class=fm.ContactForm
    template_name="schoolapp/contact.html"
    
    
    # either of :
    #success_url="/schoolapp/thanks/"
    success_url=reverse_lazy("schoolapp:nm-thanks")

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("invalid", form['name'],form['message'])
        response = super().form_invalid(form)
        response

        
        
    

    pass


# http://127.0.0.1:8000/school/createteacher/
class TeacherCreateView(CreateView):
    # note auto looks for teacher_form.html but can specify this
    # with template_name= ..   as below
    model =Teacher
    fields=['firstname', 'surname','subject']
    success_url=reverse_lazy("schoolapp:nm-thanks")
    
    # default = "schoolapp/teacher_form.html" 
    template_name="schoolapp/teacher_form_mine.html"

    pass

class TeacherListView(ListView):
    # note auto looks for teacher_list.html
    model =Teacher
    context_object_name="teacherlist"
    
    #queryset= Teacher.objects.all()
    queryset= Teacher.objects.order_by('surname')

    
class TeacherDetailView(DetailView):
    # note auto looks for teacher_detail.html
    model =Teacher

class TeacherUpdateView(UpdateView):
    # note uses same fomr as create view
    model =Teacher
    fields ="__all__"
    success_url=reverse_lazy("schoolapp:nm-listteachers")


class TeacherDeleteView(DeleteView):
    # note auto uses teacher_confirm_delete.html
    model =Teacher
    success_url=reverse_lazy("schoolapp:nm-listteachers")
