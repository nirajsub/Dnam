
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .import views

urlpatterns = [
    path('', HomeView, name = "home"),
    path('dashboard/', DashboardView, name="dashboard"),

    path('workorder/', WorkorderTaskView, name='workorder'),
    path('complaints/', ComplaintTaskView, name='complaints'),
    path('workorderupdate/<str:pk>', WorkorderUpdateView, name='workorderupdate'),
    path('complaintsupdate/<str:pk>', ComplaintsUpdateView, name='complaintsupdate'),

    path("add-work-order/", AddWorkOrderView.as_view(), name="add_work_order"),
    path("add-complaints/", AddComplaitsView.as_view(), name="add_complaints"),

    path('allclients', AllClientView, name="allclients"),
    path('addclients', AddClientView, name="addclients"),
    path('editclients/<str:pk>', EditClientView, name="editclients"),
    path('clientsite/<str:pk>', ClientSitesView, name="clientsites"),
    path('addsite/<str:pk>', AddSitesView, name="addsite"),
    path('editsite/<str:pk>', EditSitesView, name="editsite"),
    path('addworkingdays/<str:pk>', AddWorkingDaysView, name= "addworkingdays"),
    path('sitetasks/<str:pk>', SitesTaskView, name= 'sitetasks'),

    path('allemployee', AllEmployees, name="allemployee"),
    path('addemployee', AddEmployee, name="addemployee"),
    path('addsuperemployee', AddSuperEmployee, name="addsuperemployee"),
    path('editemployee/<str:pk>', EditEmployeeView, name="editemployee"),
    path('employeetasks/<str:pk>', EmployeeTasks, name = "employeetasks"),

    path('allsuperviser', AllSuperviserView, name="allsuperviser"),
    path('superviserdetail/<str:pk>', SuperviserDetailView, name="superviserdetail"),
    path('supervisertask/<str:pk>', SuperviserTaskView, name="supervisertask"),

    path('invoice', InvoiceView, name="invoice"),
    path('addinvoicein', AddInvoiceInView, name="addinvoicein"),
    path('addinvoiceout', AddInvoiceOutView, name="addinvoiceout"),

    path("superviser-register/", SuperviserRegistrationView.as_view(), name="superviser_register"),
    path("superviser-login/", SuperviserLoginView.as_view(), name="superviser_login"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
