from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment, CoepPost
from home.models import Addblog, CoepAddblog
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras



# Create your views here.

def blogHome(request): 
    allPosts= Post.objects.all()
    alld=Addblog.objects.all()
    context={'allPosts': allPosts,'postn':alld}

    return render(request, "blog/blogHome.html", context)
# change
def coepblogHome(request): 
    coepallPosts= CoepPost.objects.all()
    coepalld=CoepAddblog.objects.all()
    context={'allPosts': coepallPosts,'postn':coepalld}
    return render(request, "blog/coepblogHome.html", context)


def allblog(request):
    vallPosts= Post.objects.all()
    alld=Addblog.objects.all()
    coepallPosts= CoepPost.objects.all()
    coepalld=CoepAddblog.objects.all()
    return render(request,"blog/allblog.html",{'vallPosts': vallPosts,'postn':alld,'allPosts': coepallPosts,'postn':coepalld})

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    # post.views= post.views +1
    # post.save()    
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")

