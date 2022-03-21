from django import forms
from genero.models import Genero
class GeneroFom(forms.Form):
    
    class Meta:
        model = Genero
        fileds = "__all__"
        
