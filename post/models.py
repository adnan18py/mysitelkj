from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from products.models import *
from django.urls import reverse


class Post(models.Model):
    
    title = models.CharField(max_length=100,verbose_name='عنوان')
    text = models.TextField(null=True,verbose_name='متن')
    writer = models.CharField(max_length=30,verbose_name='نویسنده')
    img = models.ImageField(null=True,upload_to='images',verbose_name='عکس')
    alt=models.CharField(max_length=100,verbose_name='موضوع تصویر',null=True)
    crated_time = models.DateTimeField(null=True,auto_now_add=True,)
    slug = models.SlugField(null=True,max_length=50, allow_unicode=True,verbose_name='آدرس  پست',unique=True)
    tags=TaggableManager()
    related_posts = models.ManyToManyField('self', blank=True,verbose_name='پست های مشابه')
    # l=models.ManyToManyField(Products)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)
    def __str__(self):
        return '{}-{}'.format(self.pk,self.title)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

class Comment(models.Model):
    name=models.CharField(max_length=100,null=True,verbose_name='نام کاربری')
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.TextField(verbose_name='متن کامنت')


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
