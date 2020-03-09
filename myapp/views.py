from django.shortcuts import render, redirect
from myapp.models import *
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def login(request):
    return render(request,'login.html')
def check_login_details(request):
    try:
        uemail = request.POST["email"]
        upassword = request.POST["pass"]
        ucpassword=request.POST["cpass"]
        if upassword==ucpassword:
            data = Sign_up.objects.raw("select sno,email, password from user_table")
            for i in data:
                if upassword==i.password and uemail==i.email:
                    return redirect("/S_login")
    except Exception as e:
        return redirect("/login")
def sign_up(request):
    return render(request,'signup.html')
def sign_up_data_fetch(request):
    try:
        uname = request.POST["name"]
        uemail = request.POST["email"]
        upassword = request.POST["pass"]
        ucpassword=request.POST["cpass"]
        ugender=request.POST["gender"]
        ubirthday = request.POST["birthday"]
        if upassword==ucpassword:
            obj = Sign_up()
            obj.name = uname
            obj.email = uemail
            obj.password = upassword
            obj.gender=ugender
            obj.dob=ubirthday
            obj.save()
        return render(request, 'signup.html')
    except Exception as e:
        return redirect('/signup')
def s_login(request):
    return render(request,'S_login.html')
def createPost(request):
    return render(request,'createPost.html')
def editPost(request):
    try:
        data=Create_article.objects.all()
        return render(request,'editPost.html',{"mydata":data})
    except Exception as e:
        return redirect('/editPost')
def editPost_update(request):
    try:
        udescription = request.POST["description"]
        sno = request.POST["sno"]
        obj = Create_article.objects.get(sno=sno)
        obj.description = udescription
        obj.save(force_update=True)
        return redirect("/viewPost")
    except Exception as e:
        return redirect('/editPost')
def deletePost(request):
    try:
        data = Create_article.objects.all()
        return render(request,'deletePost.html',{"mydata":data})
    except Exception as e:
        return redirect('/deletePost')
def delete_post(request):
    try:
        sno = request.POST["sno"]
        obj = Create_article.objects.get(sno=sno)
        obj.delete()
        return redirect("/viewPost")
    except Exception as e:
        return redirect('/deletePost')
def viewPost(request):
    try:
        data=Create_article.objects.all()
        return render(request,'viewPost.html',{"mydata":data})
    except Exception as e:
        return redirect('/viewPost')
def searchPost(request):
    return render(request,'searchPost.html')
def searchPostresult(request):
    utitle = request.POST["title"]
    try:
        data = Create_article.objects.get(title=utitle)
        return render(request, "searchPostresult.html", {"mydata": data})
    except Exception as e:
        print("error occurred")
        return redirect("/searchPost")
def forgetpass(request):
    return render(request,'forgetpass.html')
def update_password(request):
    try:
        uemail = request.POST["email"]
        upassword = request.POST["password"]
        data = Sign_up.objects.raw("select * from user_table where email='%s'"%(uemail))
        if uemail==data[0].email:
            obj=Sign_up.objects.get(email=uemail)
            obj.password=upassword
            obj.save(force_update=True)
        return render(request,'login.html')
    except Exception as e:
        return redirect('/createPost')
    """
     for i in data:
         if uemail==i.email:
             sno = request.POST["i.sno"] #ask about that how to fetch primary key/sno from database
             obj=Sign_up()
             obj.sno=g
             obj.email=uemail
             obj.password=upassword
             obj.sno=sno
             obj.save(force_update=True)
     """
def insert_article(request):
    try:
        utitle = request.POST["title"]
        udescription = request.POST["description"]
        obj = Create_article()
        obj.title = utitle
        obj.description = udescription
        obj.save()
        return render(request, 'createPost.html')
    except Exception as e:
        return redirect('/createPost')