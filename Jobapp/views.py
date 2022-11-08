import re
from urllib import response
from django.shortcuts import redirect, render
from .models import *
from random import randint
# Create your views here.

from django.http import HttpResponse
from django.template import loader
import pdfkit
import io





def IndexPage(request):
    return render(request,"app/index.html")


def SingupPage(request):
    return render(request,"app/signup.html")

def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request,"app/signup.html",{'msg':message})
        
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
            else:
                message = "Password and Cpassword Dos't Not Match"
                return render(request,"app/signup.html",{'msg':message})

    else:
        # Company Register
        if request.POST['role']=="Company":
            role = request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
   
            user = UserMaster.objects.filter(email=email)
            
               
            if user:
                message = "User already Exist"
                return render(request,"app/signup.html",{'msg':message})
            else:
                if password == cpassword:
                    otp = randint(100000,999999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcomp = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app/otpverify.html",{'email':email})
                else:
                    message = "Password and Cpassword Doesn't Match"
                    return render(request,"app/signup.html",{'msg':message})


def OTPPage(request):
    return render(request,"app/otpverify.html")


def Otpverfy(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)
    
    if user:
        if user.otp == otp:
            message = "Otp verify successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "Otp is incorrect"
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        return render(request,"app/signup.html")

def Loginpage(request):
    return render(request,"app/login.html")


def LoginUser(request):
    if request.POST['role']=='Candidate':
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)

        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('index')
            else:
                message = "Password doesn't match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User doesn't exist"
            return render(request,"app/login.html",{'msg':message})

# Company Login
    else:
        if request.POST['role']=='Company':
            email = request.POST['email']
            password = request.POST['password']
    
            user = UserMaster.objects.get(email=email)

        if user:
            if user.password==password and user.role=="Company":
                comp = Company.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = comp.firstname
                request.session['lastname'] = comp.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('companyindex')
            else:
                message = "Password doesnot match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User doesnot exist"
            return render(request,"app/login.html",{'msg':message})


def Profilepage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user,'can':can})


def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.contact = request.POST['contact']
        can.city = request.POST['city']
        can.state = request.POST['state']
        can.country = request.POST['country']
        can.address = request.POST['email']
        can.dob = request.POST['dob']
        can.gender = request.POST['gender']
        can.min_salary = request.POST['minsalary']
        can.max_salary = request.POST['maxsalary']
        can.job_type = request.POST['jobtype']
        can.jobcategory = request.POST['jobcategory']
        can.highestedu = request.POST['education']
        can.experience = request.POST['experience']
        can.website = request.POST['website']
        can.shift = request.POST['shift']
        can.jobdescription = request.POST['jobdescription']
        can.profile_pic = request.FILES['image']
        can.save()
        print("Data SAVED")
        url = f'/profile/{pk}'
        return redirect(url)

def Candidatelogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('loginpage')

def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/job-list.html",{'alljob':all_job})

def ApplyPage(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
    return render(request,"app/apply.html",{'user':user,'cand':cand,'job':job})


def ApplyJob(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        edu = request.POST['education']
        exp = request.POST['experience']
        web = request.POST['website']
        min_salary = request.POST['minsalary']
        max_salary = request.POST['maxsalary']
        gender = request.POST['gender']
        resume = request.FILES['resume']

        newapply = ApplyList.objects.create(candidate=can,job=job,education=edu,experience=exp,website=web,min_salary=min_salary,max_salary=max_salary,gender=gender,resume=resume)
        
        message = " Job Applied successfully"
        return render(request,"app/apply.html",{'msg':message})

def JobGrid(request):
    return render(request,"app/job-grid.html")

def JobDetail(request):
    return render(request,"app/job-details.html")

def DetailJob(request):
    return render(request,"app/job-details-2.html")

def AboutPage(request):
    return render(request,"app/about.html")

def ServicesPage(request):
    return render(request,"app/services.html")

def TeamPage(request):
    return render(request,"app/team.html")

def FaqPage(request):
    return render(request,"app/faq.html")

def PricingPage(request):
    return render(request,"app/pricing.html")

def Candidates_listingPage(request):
    return render(request,"app/candidates-listing.html")

def Candidates_ProfilePage(request):
    return render(request,"app/candidates-profile.html")

def Blog_GridPage(request):
    return render(request,"app/blog-grid.html")

def Blog_SidebarPage(request):
    return render(request,"app/blog-sidebar.html")

def Blog_DetailsPage(request):
    return render(request,"app/blog-details.html")

def Employers_listPage(request):
    return render(request,"app/employers-list.html")

def Company_detailPage(request):
    return render(request,"app/company-detail.html")



def ComponentsPage(request):
    return render(request,"app/components.html")

def ContactPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/contact.html",{'user':user,'can':can})
    
def ContactSendPage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        Name = request.POST['name']
        Contact = request.POST['contact']
        Email = request.POST['email']
        Subject = request.POST['subject']
        Message = request.POST['cmmentso']
        
        sendcontact = Contactsend.objects.create(user_id=can,Name=Name,Email=Email,Contact=Contact,Subject=Subject,Message=Message)

        message = "Message Send Successfully"
        return render(request,"app/contact.html",{'msg':message})

def ForgetPage(request):
    return render(request,"app/recovery_passward.html")


   








########################## Company Side ######################

def CompanyIndexPage(request):
    return render(request,"app/Company/index.html")

def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    return render(request,"app/Company/profile.html",{'user':user,'comp':comp})

def UpdateCompanyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        comp.firstname = request.POST['firstname']
        comp.lastname = request.POST['lastname']
        comp.company_name = request.POST['companyname']
        comp.city = request.POST['city']
        comp.state = request.POST['state']
        comp.country = request.POST['country']
        comp.website = request.POST['companywebsite']
        comp.address = request.POST['companyaddress']
        comp.contact = request.POST['companycontact']
        comp.description = request.POST['companydescription']
        comp.logo_pic = request.FILES['image']
        comp.save()
        url = f"/companyprofile/{pk}"
        return redirect(url)


def JobPostPage(request):
    return render(request,"app/Company/jobpost.html")

def JobDetailSubmit(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        resposibilties = request.POST['resposibilties']
        location  = request.POST['location']
        companycontact = request.POST['companycontact']
        salarypackage = request.POST['salarypackage']
        companywebsite = request.POST['companywebsite']
        companyemail = request.POST['companyemail']
        experience  = request.POST['experience']
        logo = request.FILES['image']

        newjob = JobDetails.objects.create(company_id=comp,jobname=jobname,companyname=companyname,companyaddress=companyaddress,jobdescription=jobdescription,qualification=qualification,resposibilties=resposibilties,location=location,companyemail=companyemail,companycontact=companycontact,salarypackage=salarypackage,companywebsite=companywebsite,experience=experience,logo=logo)

        message = "Job Post successFully"
        return render(request,"app/Company/jobpost.html",{'msg':message})

def JobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/Company/jobpostlist.html",{'alljob':all_job})


def JobApplyList(request):
    all_jobapply = ApplyList.objects.all()
    return render(request,"app/Company/applyjoblist.html",{'alljob':all_jobapply})



def Companylogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('loginpage')

def DeleteCompany(request,pk):
    company1 = JobDetails.objects.get(pk=pk)
    company1.delete()
    return redirect('joblistpage')



####################### ADMIN SIDE #######################

def  AdminLoginPage(request):
    return render(request,"app/admin/login.html")

def AdminIndexPage(request):
    if 'email' in request.session and 'password' in request.session:
        return render(request,"app/admin/index.html")
    else:
        return redirect('adminloginpage')

def AdminLogin(request):
    email = request.POST['email']
    password = request.POST['password']

    if email == "saurabhkasar1799@gmail.com" and password == "1234":
        request.session['email'] = email
        request.session['password'] = password
        return redirect('adminindex')

    else:
        message = "Email and Password not Match"
        return render(request,"app/admin/login.html",{'msg':message})


def AdminUserList(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request,"app/admin/userlist.html",{'alluser':all_user})

def AdminCompanyList(request):
    all_company = UserMaster.objects.filter(role="Company")
    return render(request,"app/admin/companylist.html",{'allcompany':all_company})

def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')

def VerifyCompanyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
       return render(request,"app/admin/verify.html",{'company':company})

def VerifyCompany(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('companylist')

def CompanyDelete(request,pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')

def adminlogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('loginpage')


########################### resume ########################
def Resume(request):
#     Firstname = request.POST.get("firstname","")
#     Middlename = request.POST.get("middlename","")
#     Surname = request.POST.get("surname","")
#     Dob  = request.POST.get("dob","")
#     Sex  = request.POST.get("gender","")
#     Marital_status = request.POST.get("Status","")
#     City = request.POST.get("city","")
#     State = request.POST.get("State","")
#     Country = request.POST.get("country","")
#     Contact = request.POST.get("contact","")
#     Email = request.POST.get("email","")
#     Website= request.POST.get("website","")
#     Address = request.POST.get("address","")
#     Graduation = request.POST.get("graduation","")
#     University_college = request.POST.get("university/college","")
#     Degree_certification = request.POST.get("degree/certification","")
#     Course_title = request.POST.get("course","")
#     Additional_information = request.POST.get("addition_information","")
#     Company_name = request.POST.get("companyname","")
#     Job_position = request.POST.get("jobPosition","")
#     Location = request.POST.get("location","")
#     Date_From = request.POST.get("date_from","")
#     Date_To = request.POST.get("date_to","")
#     Skills = request.POST.get("skills","")
#     Skill_proficiency = request.POST.get("skills_proficiency","")
#     profile=Profile(Firstname=Firstname,Middlename=Middlename,Surname=Surname,Dob=Dob,Sex=Sex,Marital_status=Marital_status,City=City,State=State,Country=Country,Contact=Contact,Email=Email,Website=Website,Address=Address,Graduation=Graduation,University_college=University_college,Degree_certification=Degree_certification,Course_title=Course_title,Additional_information=Additional_information,Company_name=Company_name,Job_position=Job_position,Location=Location,Date_From=Date_From,Date_To=Date_To,Skills=Skills,Skill_proficiency=Skill_proficiency)
#     profile.save()
    return render(request,"app/create-resume.html")



# def ResumePage(request,pk):
#     user_profile = Profile.objects.get(pk=pk)
#     return render(request,"app/resume.html",{'user_profile':user_profile})
   