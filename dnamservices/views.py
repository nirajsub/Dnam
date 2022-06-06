from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .models import *

def HomeView(request):
    template_name = "dnamservices/home.html"
    service = Services.objects.all()
    context = {
        'service':service
    }
    return render(request, template_name, context)

def DashboardView(request):
    template_name = "dnamservices/dashboard/dashboard.html"
    return render(request, template_name)

def WorkorderTaskView(request):
    template_name = "dnamservices/dashboard/workordertask.html"
    workordertask = WorkOrderTask.objects.all()

    context = {
        'workordertask':workordertask,
    }
    return render(request, template_name, context)

class AddWorkOrderView(CreateView):
    template_name = 'dnamservices/dashboard/addworkorder.html'
    model = WorkOrderTask
    form_class = AddWorkOrderForm

    success_url = reverse_lazy('workorder')

    def form_valid(self, form):
        form.instance.workorder_user = self.request.user
        return super().form_valid(form)

def WorkorderUpdateView(request, pk):
    template_name = 'dnamservices/dashboard/updateworkorder.html'

    workordertask = WorkOrderTask.objects.get(id=pk)
    form = AddWorkOrderForm(instance=workordertask)
    if request.method == "POST":
        form = AddWorkOrderForm(request.POST, instance=workordertask)
        if form.is_valid():
            form.save()
        return redirect("workorder")
    context = {
        'workordertask':workordertask,
        'form':form
    }
    return render(request, template_name, context)



# def AddWorkOrderView(request):
#     template_name = 'dnamservices/dashboard/addworkorder.html'
#     usr = request.user
#     form = AddWorkOrderForm()
#     task = WorkOrderTask.objects.get_or_create(workorder_user=usr, show=False)

#     context = {
#         'task':task,
#         'form':form
#     }
#     return render(request, template_name, context)



def ComplaintTaskView(request):
    template_name = "dnamservices/dashboard/complainttask.html"
    complainttask = ComplaintTask.objects.all()

    context = {
        'complainttask':complainttask,
    }
    return render(request, template_name, context)

class AddComplaitsView(CreateView):
    template_name = 'dnamservices/dashboard/addcomplaint.html'
    model = ComplaintTask
    form_class = AddComplaintsForm

    success_url = reverse_lazy('workorder')

    def form_valid(self, form):
        form.instance.complaint_user = self.request.user
        return super().form_valid(form)

def ComplaintsUpdateView(request, pk):
    template_name = 'dnamservices/dashboard/updatecomplaints.html'

    complaintstask = ComplaintTask.objects.get(id=pk)
    form = AddComplaintsForm(instance=complaintstask)
    if request.method == "POST":
        form = AddComplaintsForm(request.POST, instance=complaintstask)
        if form.is_valid():
            form.save()
        return redirect("complaints")
    context = {
        'complaintstask':complaintstask,
       'form':form
    }
    return render(request, template_name, context)

def AllClientView(request):
    template_name = "dnamservices/dashboard/allclient.html"
    client = Client.objects.all()
    context = {
        'client':client
    }
    return render(request, template_name, context)

def AddClientView(request):
    template_name = "dnamservices/dashboard/addclient.html"
    form = AddClientForm()
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ("allclients")
    context = {
        'form':form,
    }
    return render(request, template_name, context)

def EditClientView(request, pk):
    template_name = "dnamservices/dashboard/editclient.html"
    client = Client.objects.get(id=pk)
    form = AddClientForm(instance=client)
    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
        return redirect ("allclients")
    context = {
        'client':client,
        'form':form
    }
    return render(request, template_name, context)

def ClientSitesView(request, pk):
    template_name = "dnamservices/dashboard/clientsites.html"
    client = Client.objects.get(id=pk)
    context = {
        'client':client
    }
    return render(request, template_name, context)

def AddSitesView(request, pk):
    template_name = "dnamservices/dashboard/addsites.html"
    clientid = Client.objects.get(id=pk)
    site, created = Sites.objects.get_or_create(client=clientid, enter=False)
    form = AddSitesForm(instance=site)
    if request.method == "POST":
        form = AddSitesForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
        return redirect("allclients")
    context = {
        'clientid':clientid,
        'form':form
    }
    return render(request, template_name, context)

def EditSitesView(request, pk):
    template_name = "dnamservices/dashboard/editsites.html"
    site = Sites.objects.get(id=pk)
    form = EditSitesForm(instance=site)
    if request.method == "POST":
        form = EditSitesForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
        return redirect("allclients")
    context = {
        'site':site,
        'form':form
    }
    return render(request, template_name, context)

def AddWorkingDaysView(request, pk):
    template_name = "dnamservices/dashboard/addworkingdays.html"
    site = Sites.objects.get(id=pk)
    form = AddSiteWorkingdays(instance=site)
    if request.method == "POST":
        form = AddSiteWorkingdays(request.POST, instance=site)
        if form.is_valid():
            form.save()
        return redirect("allclients")
    context = {
        'site':site,
        'form':form
    }
    return render(request, template_name, context)

def SitesTaskView(request, pk):
    template_name = "dnamservices/dashboard/sitetasks.html"
    site = Sites.objects.get(id=pk)
     
    context = {
        'site':site
    }
    return render(request, template_name, context)

def AllEmployees(request):
    template_name = "dnamservices/dashboard/allemployee.html"    
    employee = Employee.objects.all()
    context = {
        'employee':employee
    }
    return render(request, template_name, context)

def AddEmployee(request):
    template_name = "dnamservices/dashboard/addemployee.html"

    form = AddEmployeeForm()
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("allemployee")
    context = {
        'form':form,
    }
    return render(request, template_name, context)

def AddSuperEmployee(request):
    template_name = "dnamservices/dashboard/addsuperemployee.html"

    form = AddSuperviserAsEmployee()
    if request.method=="POST":
        form = AddSuperviserAsEmployee(request.POST)
        if form.is_valid():
            form.save()
        return redirect('allemployee')
    context = {
        'form':form
    }
    return render(request, template_name, context)

def EditEmployeeView(request, pk):
    template_name = "dnamservices/dashboard/editemployee.html"
    employee = Employee.objects.get(id=pk)
    form = EditEmployeeForm(instance=employee)
    
    if request.method=="POST":
        form = EditEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect("allemployee")
    
    context = {
        'form':form,
        'employee':employee
    }
    return render(request, template_name, context)

def EmployeeTasks(request, pk):
    template_name = "dnamservices/dashboard/employeetask.html"

    employee = Employee.objects.get(id=pk)

    context = {
        'employee':employee
    }
    return render(request, template_name, context)


def AllSuperviserView(request):
    template_name = "dnamservices/dashboard/allsuperviser.html"   
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request, template_name, context)

def SuperviserDetailView(request, pk):
    template_name = "dnamservices/dashboard/superviserdetail.html"
    superviser = User.objects.get(id=pk)
    context = {
        'superviser':superviser
    }
    return render(request, template_name, context)

def SuperviserTaskView(request, pk):
    template_name = "dnamservices/dashboard/supervisertask.html"
    superviser = User.objects.get(id=pk)
    context = {
        'superviser':superviser
    }
    return render(request, template_name, context)

def InvoiceView(request):
    template_name = "dnamservices/dashboard/invoice.html"
    invoicein = InvoiceIn.objects.all()
    invoiceout = InvoiceOut.objects.all()
    context = {
        'invoicein':invoicein,
        'invoiceout':invoiceout
    }
    return render(request, template_name, context)

def AddInvoiceInView(request):
    template_name = "dnamservices/dashboard/invoicein.html"
    form = AddInvoiceInForm()
    if request.method == "POST":
        form = AddInvoiceInForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("unsupported files")
        return redirect('invoice')
    context = {
        'form':form
    }
    return render(request, template_name, context)

def AddInvoiceOutView(request):
    template_name = "dnamservices/dashboard/invoiceout.html"
    form = AddInvoiceOutForm()
    if request.method == "POST":
        form = AddInvoiceOutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("unsupported files")
        return redirect('invoice')
    context = {
        'form':form
    }
    return render(request, template_name, context)


class SuperviserRegistrationView(CreateView):
    template_name = "dnamservices/accounts/superviser_register.html"
    form_class = SuperviserRegistrationForm
    success_url = reverse_lazy("superviser_login")
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Sorry! Superviser with this username already exists. please try new username.")
        if User.objects.filter(email=email).exists():
            return HttpResponse("Sorry! Superviser with this email already exists. please try new email.")
        user = User.objects.create_user(username, email, password, is_staff=True)
        form.instance.superviser_user = user
        return super().form_valid(form)
    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url

class SuperviserLoginView(FormView):
    template_name = "dnamservices/accounts/superviserlogin.html"
    form_class = SuperviserLoginForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Superviser.objects.filter(superviser_user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})
        return super().form_valid(form)
