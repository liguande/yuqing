from django import forms

class AddForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()