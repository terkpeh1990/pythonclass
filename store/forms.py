from django import forms

class BrandForm(forms.Form):
    name = forms.CharField(required=True)

