from django import forms  
from crud_app.models import Film  

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
