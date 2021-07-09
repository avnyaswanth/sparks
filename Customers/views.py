from django.shortcuts import redirect, render,HttpResponse
from .models import CustomersDetails, MyAccount
from django.contrib import messages


def getting_details_by_id(customer_id):
    customers_obj = CustomersDetails.objects.all()
    return customers_obj[customer_id-1]
# VIEWS
def homepage(request):
    return render(request,'Customers/homepage.html')

def viewcustomers(request):
    customers_obj = CustomersDetails.objects.all()
    return render(request,'Customers/viewcustomers.html',{'customers':customers_obj})

def showcustomer(request,customer_id):
    currentcustomer = getting_details_by_id(customer_id)
    return render(request,'Customers/showcustomer.html',{'curcustomer' : currentcustomer})

def transfer(request,c_id):
    currentcustomer = getting_details_by_id(c_id)
    myact = MyAccount.objects.all()[0]

    if request.method == 'POST':
        myactamount = myact.Balance
        enteredamount = request.POST.get('amount')
        if enteredamount and int(enteredamount) > 0 and int(enteredamount) <= myactamount:
            myact.Balance = myactamount-int(enteredamount)
            myact.save()
            currentcustomer.Balance += int(enteredamount)
            currentcustomer.save()
            messages.success(request,f'You have successfully sent {enteredamount} rupees to {currentcustomer.CustomerName}')
        elif enteredamount:
            messages.error(request,f'You are trying to send {int(enteredamount)}.Your Current Balance is {myact.Balance}.Please enter valid amount')
        return redirect('transfer',c_id=currentcustomer.id)

    return render(request,'Customers/transfer.html',{'curcustomer' : currentcustomer,'act' : myact})

def myaccount(request):
    myact = MyAccount.objects.all()[0]
    return render(request,'Customers/myaccount.html',{'act':myact})

def about(request):
    return render(request,'Customers/about.html')