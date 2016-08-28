from django import forms

class NameForm(forms.Form):
	admin_name = forms.CharField(label='Admin Name',max_length=100)