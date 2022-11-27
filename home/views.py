from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from home.models import Addblog
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from blog.models import Post, CoepPost

def home(request): 
    return render(request, "home/home.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
        coepPosts=CoepPost.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        # coepPostsTitle= CoepPost.objects.filter(coeptitle__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        # coepPostsAuthor= CoepPost.objects.filter(coepauthor__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        # coepPostsContent =CoepPost.objects.filter(coepcontent__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
        # coepPosts=  coepPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    # if coepPosts.count()==0:
    #     messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts,'query': query}
    return render(request, 'home/search.html', params)

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username) > 30:
            messages.error(request, " Your user name must be under 30 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def about(request): 
    return render(request, "home/about.html")

def addblog(request):
    if request.method=="POST":
        # sno=request.POST['sno']
        title=request.POST['title']
        author=request.POST['author']
        slug=request.POST['slug']
        content =request.POST['content']
        addblog=Addblog( title=title, author=author, slug=slug, content=content)
        addblog.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, "home/addblog.html")
