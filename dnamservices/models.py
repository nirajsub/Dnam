from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_location = models.CharField(max_length=50)
    client_street = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=254)
    client_website = models.CharField(max_length=50, blank=True, null=True)
    delete = models.BooleanField(("remove"), default=False)

    def __str__(self):
        return self.client_name


class Employee(models.Model):
    employee_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    superviser = models.BooleanField(default=False)
    employee_name = models.CharField(max_length=50)
    employee_contact = models.CharField(max_length=50, null=True, blank=True)
    employee_address = models.CharField(max_length=50, null=True, blank=True)
    employee_email = models.EmailField(max_length=254, null=True, blank=True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.employee_name) + "/" + str(self.id)

class Superviser(models.Model):
    superviser_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    superviser_name = models.CharField(max_length=50)
    superviser_contact = models.CharField(max_length=50)
    superviser_address = models.CharField(max_length=50)

    def __str__(self):
        return self.superviser_name

class Services(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/services')
    detail = models.TextField()
    fade = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sites(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=50, null=True, blank=True)
    site_title = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    suburb = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    site_contact = models.CharField(max_length=50, null=True, blank=True)
    site_attribute = models.CharField(max_length=100, null=True, blank=True)
    service = models.CharField(max_length=100, null=True, blank=True)
    clean_schedule = models.CharField(max_length=100, null=True, blank=True)
    clean_area = models.CharField(max_length=50, null=True, blank=True)
    clean_task_enable = models.BooleanField(null=True, blank=True)
    cleaner = models.ManyToManyField(Employee, null=True, blank=True)
    startdate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    extra_detail = models.TextField(null=True, blank=True)
    sunday = models.IntegerField(null=True, blank=True)
    monday = models.IntegerField(null=True, blank=True)
    tuesday = models.IntegerField(null=True, blank=True)
    wednesday = models.IntegerField(null=True, blank=True)
    thrusday = models.IntegerField(null=True, blank=True)
    friday = models.IntegerField(null=True, blank=True)
    saturday = models.IntegerField(null=True, blank=True)
    enter = models.BooleanField("save")
    remove = models.BooleanField("delete",default=False)

    def __str__(self):
        return self.site_name

class WorkingDays(models.Model):
    site = models.ForeignKey(Sites, on_delete=models.CASCADE, null=True, blank=True)
    sunday = models.IntegerField()
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thrusday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()

    def __str__(self):
        return self.site.site_name

class WorkOrderTask(models.Model):
    workorder_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)  
    workorder =  models.CharField(max_length=50)
    workorder_title = models.CharField(max_length=50)
    pricing = models.IntegerField()
    comments = models.CharField(max_length=50)
    assigned_to = models.ManyToManyField(Employee)
    completed_by = models.CharField(max_length=50)
    completion_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    extra_detail = models.TextField()
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.workorder

class ComplaintTask(models.Model):
    complaint_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)  
    workorder =  models.CharField(max_length=50)
    pricing = models.IntegerField()
    comments = models.CharField(max_length=50)
    assigned_to = models.ManyToManyField(Employee)
    completed_by = models.CharField(max_length=50)
    completion_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    extra_detail = models.TextField()

    def __str__(self):
        return self.workorder

class InvoiceIn(models.Model):
    name = models.CharField(max_length=50)
    in_image = models.FileField(upload_to="Invoice_in", blank=True, null = True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class InvoiceOut(models.Model):
    name = models.CharField(max_length=50)
    out_image = models.FileField(upload_to="Invoice_out", blank=True, null = True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    message = models.TextField()

    def __str__(self):
        return self.name
