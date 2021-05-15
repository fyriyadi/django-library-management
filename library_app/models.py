from django.db import models
from django.contrib.auth.models import User
import multiselectfield

class Book(models.Model):
    title = models.CharField(max_length=200,null=True)
    cover = models.ImageField(null=True, blank=True)
    author = models.ManyToManyField('Author', blank=True)
    subject = models.ManyToManyField('Subject', blank=True)
    publisher = models.ForeignKey('Publisher', null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200,null=True)
    release_date = models.DateField(null=True, blank=True,default='2021-05-15')
    types = (('Book','Book'), ('Newspapper','Newspapper'), ('Magazine','Magazine'))
    book_type = models.CharField(max_length=20, choices=types, null=True, default='Book')
    languages = (('Indonesia','Indonesia'), ('English','English'))
    language = models.CharField(max_length=20, choices=languages, null=True, default='Indonesia')
    no_of_pages = models.IntegerField(null=True, default=0)
    identifier = models.CharField(max_length=100,null=True)
    total = models.IntegerField(null=True, default=0)
    available = models.IntegerField(null=True, default=0)
    date_added =  models.DateField(null=True, blank=True, auto_now_add=True, editable=False)

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.cover.url
        except:
            url = ''
        return url


class Publisher(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=100,null=True)
    adress = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100,null=True)
    # bio
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class Borrow(models.Model):
    book = models.ForeignKey('Book', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    request_date = models.DateField(null=True, blank=True, auto_now_add=True)
    start_date = models.DateField(null=True, blank=True,default='2021-05-15')
    finish_date = models.DateField(null=True, blank=True,default='2021-05-15')
    approval_status = models.BooleanField(default=False, null=True, blank=False)
    return_status = models.BooleanField(default=False, null=True, blank=False)
    notes = models.CharField(max_length=200, null=True, default='')

    def __str__(self):
        return '%s | %s' % (self.book, self.user)



