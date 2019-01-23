from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Report
from .forms import ReportForm
from django.urls import reverse, reverse_lazy
from django.core.mail import EmailMessage
from django.db.models import Q



# def index(request):
# 	email = EmailMessage(
#     'Hello',
#     'Body goes here',
#     'admin@rammyblog.com.ng',
#     ['famununawi@321-email.com'],
#     reply_to=['tunde@rammyblog.com.ng'],
#     headers={'Message-ID': 'foo'},
# )
# 	email.send()
# 	return render(request, 'eyewitness/index.html')


class ReportList(generic.ListView):
	models = Report
	paginate_by = 10
	template_name = 'eyewitness/index.html'
	context_object_name = 'reports'


	def get_queryset(self):
		return Report.objects.filter(pub=True).order_by('date_pub')


class ReportListForAdmin(generic.ListView):
	models = Report
	paginate_by = 10
	template_name = 'eyewitness/allpost.html'
	context_object_name = 'reports'

	def get_queryset(self):
		return Report.objects.all()

def search(request):
	try:
		if request.method == 'GET':
			new_search = Blogpost.objects.filter(Q(name__icontains = request.GET['q']) |
		 Q(subject__icontains= request.GET['q']) | Q(message__icontains = request.GET['q']) ).exclude(
		 pub = False
				)
		if new_search:
			context = {'new_search':new_search}
			return render(request, 'rammyblog/search.html', context)
		else:
			return render(request, 'rammyblog/search.html')

	except MultiValueDictKeyError as e:
		return render(request, 'rammyblog/404.html')


# class CreateReport(generic.CreateView):
# 	model = Report
# 	fields = ('name','email', 'subject', 'location' , 'message', 'file')
# 	template_name = 'eyewitness/reportform.html'

# 	def get_success_url(self):
# 		"""Return the URL to redirect to after processing a valid form."""
# 		if self.success_url:
# 			url = self.success_url.format(**self.object.__dict__)
# 		else:
# 			try:
# 				url = self.object.get_absolute_url()
# 			except AttributeError:
# 				raise ImproperlyConfigured(
#                 	"No URL to redirect to.  Either provide a url or define"
#                 	" a get_absolute_url method on the Model.")

# 		email = EmailMessage(
# 				'Hello'+self.name,
# 				'Body goes here',
# 				'admin@rammyblog.com.ng',
# 				[str(self.email)],
# 				reply_to=['tunde@rammyblog.com.ng'],
# 				headers={'Message-ID': 'foo'},

# 			)
# 		email.send()
# 		name
# email
# subject
# location
# message
# file
# 		return url



def reportForm_(request):
	if request.method == 'POST':
		form = ReportForm(request.POST, request.FILES)
		print('full_report')
		if form.is_valid():
			full_report = form.save(commit=False)
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']

			
			form.save()

			email = EmailMessage(
				'Hello'+ name,
				'Hello '+ name + 'message'

				,
				'admin@rammyblog.com.ng',
				[str(email)],
				reply_to=['tunde@rammyblog.com.ng'],
				headers={'Message-ID': 'foo'},

			)
			email.send()
			hello = redirect('details', full_report.slug)
			print(hello.url)
			print(full_report.get_absolute_url())
			return redirect('details', full_report.slug)
	else:
		form =ReportForm()
	context = {'form':form}
	return render(request, 'eyewitness/reportform.html', context)


			# name = full_report.cleaned_data['name']
			# email = full_report.cleaned_data['email']
			# subject = full_report.cleaned_data['subject']
			# message = full_report.cleaned_data['message']
			# slug = full_report.cleaned_data['slug']
			

			# email = EmailMessage(
			# 	'Hello'+name,
			# 	message,
			# 	'admin@rammyblog.com.ng',
			# 	[str(email)],
			# 	reply_to=['tunde@rammyblog.com.ng'],
			# 	headers={'Message-ID': 'foo'},

			# )
			# email.send()





class ReportDetail(generic.DetailView):
	model = Report
	template_name = 'eyewitness/detail.html'
	context_object_name = 'report'


class DeleteDetail(generic.DeleteView):
	model = Report
	template_name = 'eyewitness/delete.html'
	context_object_name = 'report'
	success_url = 'all'


def publish_report(request, slug):
	report = get_object_or_404(Report, slug = slug)
	email = EmailMessage(
				'Hello'+ report.name,
				'Hello '+ report.name + report.message
				,
				'admin@rammyblog.com.ng',
				[str(report.email)],
				reply_to=['tunde@rammyblog.com.ng'],
				headers={'Message-ID': 'foo'},

			)	
	
	report.publish()
	email.send()
	return redirect('details' , slug = slug)