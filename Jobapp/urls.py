from unicodedata import name
from django.urls import path,include
from . import views 

urlpatterns = [
    path("",views.IndexPage,name="index"),
    path("signup/",views.SingupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.Otpverfy,name="otp"),
    path("loginpage",views.Loginpage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.Profilepage,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("candidatelogout/",views.Candidatelogout,name="candidatelogout"),
    path("joblist/",views.CandidateJobListPage,name="joblist"),
    path("apply/<int:pk>",views.ApplyPage,name="apply"),
    path("applyjob/<int:pk>",views.ApplyJob,name="applyjob"),
    path("Jobgrid/",views.JobGrid,name="jobgrid"),
    path("jobdetails/",views.JobDetail,name="jobdetails"),
    path("detailsjob/",views.DetailJob,name="detailsjob"),
   
    path("about/",views.AboutPage,name="about"),
    path("services/",views.ServicesPage,name="services"),
    path("team/",views.TeamPage,name="team"),
    path("faq/",views.FaqPage,name="faq"),
    path("pricing/",views.PricingPage,name="pricing"),
    path("candidateslisting/",views.Candidates_listingPage,name="candidateslisting"),
    path("candidatesprofile/",views.Candidates_ProfilePage,name="candidatesprofile"),
    path("bloggrid/",views.Blog_GridPage,name="blog_grid"),
    path("blogsidebar/",views.Blog_SidebarPage,name="blog_sidebar"),
    path("blogdetails/",views.Blog_DetailsPage,name="blog_details"),
    path("employerslist/",views.Employers_listPage,name="employerslist"),
    path("companydetails/",views.Company_detailPage,name="companydetails"),
    path("components/",views.ComponentsPage,name="components"),
    path("contactpage/<int:pk>",views.ContactPage,name="contactpage"),
    path("contactsendpage/<int:pk>",views.ContactSendPage,name="contactsendpage"),
    path("forgetpass/",views.ForgetPage,name="forgetpass"),


    path("resume/",views.Resume,name="resume"),
    # path("resumepage/<int:pk>",views.ResumePage,name="resumepage"),


    
    
   



################################# Company #########################
    
    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>",views.UpdateCompanyProfile,name="updatecompanyprofile"),
    path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
    path("jobpost/<int:pk>",views.JobDetailSubmit,name="jobpost"),
    path("joblistpage/",views.JobListPage,name="joblistpage"),
    path("companylogout/",views.Companylogout,name="companylogout"),
    path("applyjoblist/",views.JobApplyList,name="applylist"),
    path("companydelete/<int:pk>",views.DeleteCompany,name="companydelete"),


############################### Admin #######################
    
    path("adminloginpage/",views.AdminLoginPage,name="adminloginpage"),
    path("adminindex/",views.AdminIndexPage,name="adminindex"),
    path("adminlogin/",views.AdminLogin,name="adminlogin"),
    path("adminuserlist/",views.AdminUserList,name="userlist"),
    path("admincompanylist/",views.AdminCompanyList,name="companylist"),
    path("deleteuser/<int:pk>",views.UserDelete,name="deleteuser"),
    path("verifycompanypage/<int:pk>",views.VerifyCompanyPage,name="verifypage"),
    path("verifycompany/<int:pk>",views.VerifyCompany,name="verify"),
    path("deletecomapny/<int:pk>",views.CompanyDelete,name="deletecompany"),
    path("adminlogout/",views.adminlogout,name="adminlogout"),
    
]