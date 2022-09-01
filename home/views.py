# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
from multiprocessing import context
from django.shortcuts import render, redirect 
from .models import *
from .forms import CustomerForm
# from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only

# @unauthenticated_user
# def registerPage(request):

# 	form = CreateUserForm()
# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('cuts_name')


# 			messages.success(request, 'Account was created for ' + username)

# 			return redirect('login')
		

# 	context = {'form':form}
# 	return render(request, 'signup_form.html', context)







# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login_form.html')

def rooms(request):
    return render(request,'rooms.html')

def home(request):
    return render(request,'index.html')

def account_creation(request):
    form=CustomerForm
    context={
        'form':form
    }
    return render(request,'creation.html',context)





# def account_registartion(request):
#     form = SignUpForm(request.POST) 
        # cuts_name=request.POST['cuts_name']
        # cuts_lastname=request.POST['cuts_lastname']
        # address=request.POST['cuts_address']
        # ph=request.POST['cuts_ph']
        # email=request.POST['cuts_email']
        # password=request.POST['cuts_password']
        # id_proof_no=request.POST['cuts_id_proof_no']
        # id_proof_type=request.POST['id_proof_type']
        # gender=request.POST["gender"]
        # uploaded_img=request.FILES['cuts_image']

        # query=Customer_tb(
        #     cuts_name=cuts_name+" "+cuts_lastname,
        #     cuts_address=address,
        #     cuts_ph=ph,
        #     email=email,
        #     cuts_password=password,
        #     id_proof_number=id_proof_no,
        #     cuts_image=uploaded_img,
        #     id_proof_type=id_proof_type,
        #     gender=gender,)
        # query.save()
    # return render(request,'signup_form.html')


