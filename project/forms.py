from django import forms

class Form(forms.Form):
    user_rewiew = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-white'}),required=True)