from django.shortcuts import render, HttpResponse , get_object_or_404 , redirect
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *


# Create your views here.
def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


# def resume(request):
#      fm=ResumeForm()            
#      return render(request,"resume.html",{'form':fm})

def contact(request):
    return render(request, "contacts.html")


class createResume(View):
    def get(self,request):
        fm=ResumeForm()            
        return render(request,"resume.html",{'form':fm})

    def post(self,request):
        fm=ResumeForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Data Saved Successfully")
        return render(request,"resume/resumeTemp1.html",{'form':fm})

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, "Congratulations! Registration Successful!")
            form.save()
        return render(request, 'account/register.html', {'form': form})


# class ProfileViewEdit(UpdateView):
#     model = Resume
#     fields = ['first_name', 'last_name', 'address', 'age', 'dob', 'sscSchoolName', 'sscPercentage', 'hscPercentage',
#               'hscSchoolName', 'graduationPercentage', 'graduationCollegeName', 'experience', 'career_objective',
#               'skills', 'contacts']
#     template_name = "pages/profile.html"
#     success_url = "main:profile"
#
#     def get_queryset(self):
#         return

@login_required()
def profile_view_and_update(request , pk):
    profile = get_object_or_404(Resume , user=pk)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(instance=profile , data=request.POST)
        if form.is_valid():
            form.save()
            return  redirect("main:profile" , pk=pk)
    else:
        return render(request , "pages/profile.html" , {"form" : form})
