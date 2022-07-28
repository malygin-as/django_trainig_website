from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))
    phone = forms.CharField(max_length=15)