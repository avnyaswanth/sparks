from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('viewcustomers/',views.viewcustomers,name='viewcustomers'),
    path('about/',views.about,name='about'),
    path('<int:customer_id>/showcustomer/',views.showcustomer,name='showcustomer'),
    path('<int:c_id>/transfer/',views.transfer,name='transfer'),
    path('myaccount/',views.myaccount,name='myaccount'),
]