from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView
from .models import Agent, Admina, Store, MyUser
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import  AgentSignUpForm, StoreSignUpForm, AdminaSignUpForm, AgentForm,  StoreForm,  AdminaForm
from pathlib import Path
from django.http import HttpResponse
import os
from purchase.models import Message



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'aboutus.html')

def Login_C(request):
    return render(request, 'login_C.html')

def Register_C(request):
    return render(request, 'register_c.html')

class  AgentSignUpView(FormView):
    model = Agent
    form_class = AgentSignUpForm
    template_name = 'registration/signup_form.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('agent_profile')

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        Agent.gen(user)
        Agent.code(user)
        return super(AgentSignUpView, self).form_valid(form)

class  StoreSignUpView(FormView):
    model = Store
    form_class = StoreSignUpForm
    template_name = 'registration/signup_form.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('store_profile')

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'store'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        Store.gen(user)
        return super(StoreSignUpView, self).form_valid(form)

class  AdminaSignUpView(FormView):
    model = Admina
    form_class = AdminaSignUpForm
    template_name = 'registration/signup_form.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('admina_profile')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admina'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        Admina.gen(user)
        return super(AdminaSignUpView, self).form_valid(form)
   
class AgentLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('agent_profile') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class StoreLoginView(LoginView):
    template_name = 'login_S.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('store_profile') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class AdminaLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('admin_profile') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


def LogoutView(request):
    logout(request)
    return render(request, 'home.html')

@login_required
def Agentpage(request):
    user_form = AgentForm(instance=request.user)
    return render(request = request, template_name ="agent_profile.html", context = {"user":request.user, 
        "user_form": user_form})

@login_required
def Storepage(request):
    user_form = StoreForm(instance=request.user)
    return render(request = request, template_name ="store_profile.html", context = {"user":request.user, 
        "user_form": user_form})

@login_required
def Adminapage(request):
    user_form = AdminaForm(instance=request.user)
    return render(request = request, template_name ="admina_profile.html", context = {"user":request.user, 
        "user_form": user_form})

@login_required
def download_img(request, filename=''):
    usr = request.user
    filename = usr.phone
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '/media/user_qr/' + filename + '.png'
    path = open(filepath, 'rb')
    response = HttpResponse(path, content_type='image/png')
    response['Content-Disposition'] = "attachment; filename=%s" % filename + '.png'
    return response

@login_required
def view_conversationS(request):
    messages = Message.objects.filter(sender=request.user).order_by('timestamp')
    count = messages.count()
    return render(request, 'chatS.html', {'messages': messages, 'count': count})

@login_required
def view_conversationA(request):
    messages = Message.objects.filter(recipient=request.user).order_by('timestamp')
    count = messages.count()
    return render(request, 'chatA.html', {'messages': messages, 'count': count})