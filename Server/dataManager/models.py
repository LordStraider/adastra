from django.db import models


class Menu(models.Model):
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __unicode(self):
        return self.text


class DropDown(models.Model):
    Menu = models.ForeignKey(Menu)
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __unicode(self):
        return self.text


class Content(models.Model):
    text = models.TextField()
    site = models.CharField(max_length=200)

    def __unicode(self):
        return self.text
