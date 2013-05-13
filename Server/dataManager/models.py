from django.db import models
from django import forms


class User(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class Menu(models.Model):
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text

    @classmethod
    def create(cls, text, link):
        Menu = cls(text=text, link=link)
        Menu.save()


class DropDown(models.Model):
    Menu = models.ForeignKey(Menu)
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    hasFiles = models.BooleanField()

    def __unicode__(self):
        return self.text

    @classmethod
    def create(cls, menu, text, link, hasFiles):
        DropDown = cls(Menu=menu, text=text, link=link, hasFiles=hasFiles)
        DropDown.save()


class Content(models.Model):
    text = models.TextField()
    site = models.CharField(max_length=200)

    def __unicode__(self):
        return self.site

    @classmethod
    def create(cls, text, site):
        Content = cls(text=text, site=site)
        Content.save()
