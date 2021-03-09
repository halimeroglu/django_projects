from django import forms
from .models import *


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class NoteForms(forms.ModelForm):
    class Meta:
        model= NoteForm
        fields = '__all__'   