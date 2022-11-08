from distutils.command.upload import upload
from email.message import Message
from email.policy import default
from pyexpat import model
from django.db import models


# Create your models here.
class UserMaster (models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)


class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    min_salary = models.BigIntegerField(default=0)
    max_salary = models.BigIntegerField(default=0)
    job_type = models.CharField(max_length=150,default="")
    jobcategory = models.CharField(max_length=150,default="")
    highestedu = models.CharField(max_length=150,default="")
    experience = models.CharField(max_length=150,default="")
    website = models.CharField(max_length=150,default="")
    shift = models.CharField(max_length=150,default="")
    jobdescription = models.CharField(max_length=150,default="")
    profile_pic = models.ImageField(upload_to="app/img/candidate")


class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    website = models.CharField(max_length=250,default="")
    description = models.CharField(max_length=500,default="")
    logo_pic = models.ImageField(upload_to="app/img/Company")


class JobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.TextField(max_length=500)
    qualification = models.CharField(max_length=250)
    resposibilties = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=250)
    companyemail = models.CharField(max_length=250)
    companycontact = models.CharField(max_length=20)
    salarypackage = models.CharField(max_length=250)
    experience = models.IntegerField()
    logo = models.ImageField(upload_to="app/img/jobpost",default="")


class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    education = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)
    website = models.CharField(max_length=200)
    min_salary = models.CharField(max_length=200)
    max_salary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    resume = models.FileField(upload_to="app/resume")

# Contact
class Contactsend(models.Model):
    user_id = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    Name = models.CharField(max_length=150)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Subject = models.TextField(max_length=200)
    Message = models.TextField(max_length=500)


# Profile Resume
# class Profile(models.Model):
#     Firstname = models.CharField(max_length=50)
#     Middlename = models.CharField(max_length=50)
#     Surname = models.CharField(max_length=50)
#     Dob = models.CharField(max_length=50)
#     Sex = models.CharField(max_length=50)
#     Marital_status = models.CharField(max_length=150,default="")
#     City = models.CharField(max_length=50)
#     State = models.CharField(max_length=50)
#     Country = models.CharField(max_length=50)
#     Contact = models.CharField(max_length=50)
#     Email = models.EmailField(max_length=50)
#     Website = models.CharField(max_length=250,default="")
#     Address = models.CharField(max_length=150)
#     Graduation = models.CharField(max_length=150)
#     University_college = models.CharField(max_length=150)
#     Degree_certification = models.CharField(max_length=150)
#     Course_title = models.CharField(max_length=150)
#     Additional_information = models.CharField(max_length=150)
#     Company_name = models.CharField(max_length=150)
#     Job_position = models.CharField(max_length=50)
#     Location = models.CharField(max_length=150)
#     Date_From = models.CharField(max_length=50)
#     Date_To = models.CharField(max_length=50)
#     Skills = models.CharField(max_length=150)
#     Skill_proficiency = models.CharField(max_length=150)



    
