from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by " + self.author
# change
class CoepPost(models.Model):
    coepsno=models.AutoField(primary_key=True)
    coeptitle=models.CharField(max_length=255)
    coepauthor=models.CharField(max_length=14)
    coepcontent=models.TextField()
    coepslug=models.CharField(max_length=130)
    coepviews= models.IntegerField(default=0)
    coeptimeStamp=models.DateTimeField(blank=True)



    def __str__(self):
        return self.coeptitle + " by " + self.coepauthor

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

# class Addblog(models.Model):
#     sno= models.AutoField(primary_key=True)
#     title=models.CharField(max_length=255)
#     author=models.CharField(max_length=14)
#     slug=models.CharField(max_length=130)
#     content=models.TextField()


    
