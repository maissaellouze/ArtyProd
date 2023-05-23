from django import forms
from .models import Projet
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()


class ProjetForm(forms.Form):
    class Meta:
        model = Projet
        fields = ('libelle', 'description', 'date_debut', 'date_fin', 'equipe')


