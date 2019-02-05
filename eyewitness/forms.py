from django.forms import ModelForm, Textarea, TextInput, FileInput
from .models import Report, Comment

class ReportForm(ModelForm):
	# message = forms.CharField(widget=forms.Textarea(attrs = {'class':'form-control'}))
	# file = forms.ImageField(label='Upload an Image')
	class Meta:
		model = Report
		fields = ('name','email', 'subject','location',  'message', 'file' )
		widgets ={
				'message': 	Textarea(attrs = {'tabindex':'4', 'rows':"5" ,'cols':"50",  'placeholder':"Message...", 'class':"common-input mb-20 form-control"}),
				'email' : TextInput(attrs = {'name':"email", 'placeholder':"Enter email address",'class':"common-input mb-20 form-control", 'tabindex':"2"}),
				'name' : TextInput(attrs = {'name':"name", 'class':"form-control" , 'placeholder':'Your name','tabindex':"1"}),
				'location' : TextInput(attrs = {'name':"location", 'class':"form-control" , 'placeholder':'Enter Your Location','tabindex':"1"}),
				'subject' : TextInput(attrs = {'name':"subject", 'class':"form-control" , 'placeholder':'Post Title','tabindex':"1"}),
				'file' : FileInput(attrs = {'name':"file", 'class':"form-control" , 'placeholder':'Upload an Image','tabindex':"1"}),
				}
				




class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('name','message' )
		widgets ={
				'message': 	Textarea(attrs = {'class':'form-control'}),
				}



  # widgets = {""
  #           'name': Textarea(attrs={'cols': 80, 'rows': 20}),
  #       }

   