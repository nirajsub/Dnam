
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class SuperviserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    # email = forms.CharField(widget=forms.EmailInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = Superviser
        fields = ["superviser_name", "superviser_contact", "superviser_address"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            return HttpResponse("Sorry! Superviser with this username already exists. please try new username.")
            raise forms.ValidationError(
                "Sorry! Superviser with this username already exists. please try new username.")
        return uname
    
class SuperviserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class AddWorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrderTask
        fields = '__all__'
        exclude = ['workorder_user']

class AddComplaintsForm(forms.ModelForm):
    class Meta:
        model = ComplaintTask
        fields = '__all__'
        exclude = ['complaint_user']
    
class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_contact', 'employee_address', 'employee_email']

class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_contact', 'employee_address', 'employee_email' , 'delete']

    
class AddSuperviserAsEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_user', 'superviser', 'employee_name']


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    
class AddSitesForm(forms.ModelForm):
    class Meta:
        model = Sites
        fields = '__all__'
        exclude = ['client', 'sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'remove']

class EditSitesForm(forms.ModelForm):
    class Meta:
        model = Sites
        fields = '__all__'
        exclude = ['client', 'sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'enter']
    
class AddSiteWorkingdays(forms.ModelForm):
    class Meta:
        model = Sites
        fields = ['sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday']

class AddInvoiceInForm(forms.ModelForm):
    class Meta:
        model = InvoiceIn
        exclude = ['delete']

class AddInvoiceOutForm(forms.ModelForm):
    class Meta:
        model = InvoiceOut
        fields = '__all__'
        exclude = ['delete']
