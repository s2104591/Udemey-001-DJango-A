from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book,Author,BookInstance,Genre,Language 
from django.views.generic import CreateView,DetailView,ListView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy, reverse 

from django.contrib.auth.models import User

#http://127.0.0.1:8000/

# Create your views here.
def indexMine(request):
    num_books= Book.objects.all().count() 
    num_instances = BookInstance.objects.all().count() 

    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail
    }

    return render(request,'appcatalog/indexMine.html',context=context)



# Create your views here.
def index(request):

    num_books= Book.objects.all().count() 
    num_instances = BookInstance.objects.all().count() 

    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail
    }

    return render(request,'appcatalog/index.html',context=context)


def testa(request):
    dictparam ={ 'message':"Hello 200"}

    return render(request,'appcatalog/testa.html',context=dictparam)


    


def mycreatebook(request):    
    #example
    #return redirect (reverse('carapp:nm-listcars'))
    #return redirect(reverse('appcatalog:nm-createbook'))
    print("**************")
    uname = request.user.username
    ugroup= request.user.groups.all()
    ustaff=request.user.is_staff

    print("staff",ustaff)
    print("current user=",uname)
    print("usergroup=",ugroup)
    
    if ustaff:
        return redirect(reverse('nm-createbook'))
    else:
        return redirect(reverse('nm-index'))




class BookCreate(LoginRequiredMixin,CreateView): 
#class BookCreate(CreateView): 
    

    #book_form.html
    model = Book 
    fields = '__all__'

class BookDetail(DetailView):
    model = Book 

@login_required 
def requireslogin(request):
    #  http://127.0.0.1:8000/catalog/requireslogin 
    
    # my experimanting
    # user =User.objects.get() 
    # print("user-name" , user.get_username )

    return render(request,'appcatalog/my_view.html')


class MarianoSignUpView(CreateView):
    model=User
    success_url = reverse_lazy('login')
    template_name = 'appcatalog/signup.html'
    fields="__all__"
    #fields=['username','password']




class SignUpView(CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'appcatalog/signup.html'

class CheckedOutBooksByUserView(LoginRequiredMixin,ListView):
    # List all BookInstances BUT I will filter based off currently logged in user session
    model = BookInstance 
    template_name = 'appcatalog/profile.html'
    paginate_by = 5 # 5 book instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user) 

    

