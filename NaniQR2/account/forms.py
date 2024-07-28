from django import forms
from .admin import AgentCreationForm, StoreCreationForm
from .models import Agent, Admina, Store

class AgentSignUpForm(AgentCreationForm):
    class Meta:
        model = Agent
        fields = ['phone', 'name', 'product']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_agent = True
        if commit:
            user.save()
        return user

class StoreSignUpForm(StoreCreationForm):
    class Meta:
        model = Store
        fields = ['phone', 'name',  'address', 'description', 'product']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_store = True
        if commit:
            user.save()
        return user

class AdminaSignUpForm(AgentCreationForm):
    class Meta:
        model = Admina
        fields = ['phone', 'name']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admina = True
        if commit:
            user.save()
        return user

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['phone', 'name'] 

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['phone', 'name', 'address', 'description'] 

class AdminaForm(forms.ModelForm):
    class Meta:
        model = Admina
        fields = ['phone', 'name'] 