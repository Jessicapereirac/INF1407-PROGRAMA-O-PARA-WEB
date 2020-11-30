from django.db import models


class User(models.Model):
    name = models.CharField("Name", max_length=80)
    email = models.CharField("Email", max_length=80)
    password = models.CharField("Password", max_length=20)


class Request(models.Model):
    name = models.CharField('Name', max_length=100)
    base_url = models.CharField('URLBase', max_length=200)
    date = models.CharField('Date', max_length=50)
    relevance = models.CharField('Relevance', max_length=50)

    def __str__(self):
        return self.nome