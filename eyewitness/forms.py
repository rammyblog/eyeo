from django.forms import ModelForm, Textarea
from .models import Report

class ReportForm(ModelForm):
	# message = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control'}))
	# file = forms.ImageField(label='Upload an Image')
	class Meta:
		model = Report
		fields = ('name','email', 'subject','location',  'message', 'file' )
		widgets ={
				'message': 	Textarea(attrs = {'class':'form-control'}),
				}



  # widgets = {
  #           'name': Textarea(attrs={'cols': 80, 'rows': 20}),
  #       }