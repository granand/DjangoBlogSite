from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
   # author connected to the super use of the website
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

        # django expects the function name to be get_absolute_url
    def get_absolute_url(self):
        # After we create a post where should I go...
        # go to the url post_detail with the primary key of the post that you just created
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # django expects the function name to be get_absolute_url
    def get_absolute_url(self):
    # After the comment is created where should I go...
    # go to the list of all the posts
        return reverse("post_list")

    def __str__(self):
        return self.text
