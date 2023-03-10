from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager


from PIL import Image

class ArticleColumn(models.Model):
    """
    ArticleColumn Model
    """
    title = models.CharField(max_length=100, blank=True)
    
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    """
    Article Model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)

    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )

    # article tags
    tags = TaggableManager(blank=True)

    # article title   
    title = models.CharField(max_length=100)

    #article text
    body = models.TextField()

    # views
    total_views = models.PositiveIntegerField(default=0)

    # likes
    likes = models.PositiveIntegerField(default=0)

    # created time 
    created = models.DateTimeField(default=timezone.now)

    # updated time
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    def save(self, *args, **kwargs):
        article = super(ArticlePost, self).save(*args, **kwargs)

        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article

    def was_created_recently(self):
        diff = timezone.now() - self.created
        
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            return True
        else:
            return False