from django.db import models
from datetime import date
from pyexpat import model
from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.models import User

from django.utils import timezone
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
class Equipe(models.Model):
    nom = models.CharField(max_length=255)

    Img = models.ImageField(upload_to='media/', null=True, blank=True)


    def _str_(self):
        return (self.nom+","+self.membres)
class Personnel(models.Model):
    nom = models.CharField(max_length=255)
    skill = models.TextField(blank=True)
    ficher= models.FileField(upload_to='media/', blank=True)
    Img = models.ImageField(upload_to='media/', blank=True)
    lien_linkedIn = models.URLField(blank=True)
    Equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def _str_(self):
        return (self.nom+","+self.lien_linkedIn)
    
class Projet(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    acheve = models.BooleanField(default=False)
    equipe = models.ForeignKey('Equipe', on_delete=models.PROTECT)
    pourcentage = models.CharField(max_length=255)
    Img = models.ImageField(upload_to='media/', null=True, blank=True)

class demande_projet(models.Model):
    
    Personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    Projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    approvee = models.BooleanField(default=False)
    refuse = models.BooleanField(default=False)




class Service(models.Model):
    TYPE_CHOICES = (
        ('Product Design', 'Product Design'),
        ('UX UI Design','UX UI Design'),
        ('Branding','Branding'),
        ('Digital Strategy','Digital Strategy'),
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    Img = models.ImageField(upload_to='media/', null=True, blank=True)


    def _str_(self):
        return (self.type+","+self.description)

class Detail(models.Model):
    fichier = models.FileField(upload_to='media/')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Projet = models.ForeignKey(Projet, on_delete=models.CASCADE , default=1)
    def _str_(self):
        return (self.fichier+","+self.service+","+self.Projet)

class ProjetRequest(models.Model):
    projet = models.ForeignKey('Projet', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any additional fields specific to the project request
    # For example, you can include fields like status, additional details, etc.
    status = models.CharField(max_length=20, default='pending')
    additional_details = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.projet.libelle}"
    


class Tache(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    personne = models.ForeignKey(Personnel, on_delete=models.CASCADE,null=True, blank=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date_depot = models.DateField(null=True, blank=True)    
    Img = models.ImageField(upload_to='media/', null=True, blank=True)


    def __str__(self):
        return (self.nom +","+self.description)



class Blog (models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    texte=models.TextField(default='Non définie')
    Img = models.ImageField(upload_to='media/', null=True, blank=True)
    date_depot = models.DateField(default=timezone.now, null=True, blank=True) 


