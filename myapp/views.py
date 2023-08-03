from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .models.userInfo import UserInfo
from django.contrib.auth.hashers import make_password,check_password

from myapp.forms import todoform
from .models.todo import TODO

# Create your views here.
def home(request):
    form=todoform()
    auth_user_id=None
    user_name=None
    auth_user=None
    auth_user_id=request.session.get('customer_id')
    
    auth_user=request.session.get('customer')
    if auth_user:
        user_name=UserInfo.objects.get(email=auth_user)
    
    if auth_user:
        todo=TODO.objects.filter(user=auth_user_id).order_by('priority')
        return render(request,"base.html",{'form':form,'todos':todo,})
    return render(request,"base.html",{'form':form,'user':user_name})



class Login(View):
    def get(self,request):
        
        return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('useremail')
        password=request.POST.get('userpassword')
        
        error_msg=None
        if UserInfo.is_exit(email):
            correct_user=UserInfo.objects.get(email=email)
            
            if check_password(password,correct_user.password):
                request.session['customer'] = correct_user.email
                request.session['customer_id'] = correct_user.id
                request.session['email'] = correct_user.email
                
                
            else:
                error_msg="may Email or password Not Exist "
                return render(request, 'login.html',{'error':error_msg})
        else:
            error_msg="Email  Not Exist "
            return render(request, 'login.html',{'error':error_msg})
        
        return redirect('home')

        
    
class Signin(View):
    def get(self,request):
        return render(request,"signin.html")
    def validation(user):
        errormsg=None
        if not user.fname:
            errormsg="first name required"
        elif not user.lname:
            errormsg="last Name required"
        elif not user.email:
            errormsg="email required"
        elif not user.password:
            errormsg="set your password "
        elif len(user.password)<6:
            errormsg="password must be minimum of 6 charecter "
        elif UserInfo.objects.filter(email=user.email):
            errormsg = "Email already taken"
        return errormsg
        
    def post(self,request):
        fname=self.request.POST.get('fname')
        lname=self.request.POST.get('lname')
        email=self.request.POST.get('email')
        password=self.request.POST.get('password')
        userdata=UserInfo(fname=fname,lname=lname,email=email,password=password)
        errormsg=Signin.validation(user=userdata)
        if errormsg:
            return render(request,"signin.html",{'error':errormsg})
        else:
            password=make_password(password)
            userdata=UserInfo(fname=fname,lname=lname,email=email,password=password)
            userdata.save()
            return redirect('home')




class AddToDo(View):
    def post(self,request):
        user=request.session['customer_id']
        
        
        if UserInfo.is_exit(user):
            user_id=UserInfo.objects.filter(email=user)
            
        
            
            form=todoform(request.POST)
            if form.is_valid():
                # print(form.cleaned_data)
                # print(user_id)
                todo=form.save(commit=False)
                todo.user_id=user
                form.save()
                
                return redirect('home')
            else:
                form=todoform()
                return render(request,"base.html",{'form':form})

def del_todo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')
def change_status(request,id ,status):
    todo=TODO.objects.get(pk=id)
    todo.status=status
    todo.save()
    return redirect("home")
def logout(request):
    try:
        del request.session['customer']
    except:
        return redirect('home')
    return redirect('login')
    
    
    # return redirect("home")
    
    
        
        

        
    