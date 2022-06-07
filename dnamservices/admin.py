from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Services)
admin.site.register(Superviser)
admin.site.register(Sites)
admin.site.register(WorkOrderTask)
admin.site.register(ComplaintTask)
admin.site.register(WorkingDays)
admin.site.register(InvoiceIn)
admin.site.register(InvoiceOut)
admin.site.register(Contacts)
