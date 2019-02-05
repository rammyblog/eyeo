from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Report, Comment
from .forms import ReportForm,CommentForm
from django.urls import reverse, reverse_lazy
from django.core.mail import EmailMessage
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from .email import send_mail_submit ,send_mail_publish
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


# class ReportList(generic.ListView):
# 	models = Report
# 	paginate_by = 10
# 	template_name = 'eyewitness/magazine/index.html'
# 	context_object_name = 'reports'

# 	def get_queryset(self):
# 		return Report.objects.filter(pub=True).order_by('date_pub')

def index(request):
	report = Report.objects.filter(pub=True).order_by('date_pub')
	picks =  Report.objects.filter(Q(pub=True) & Q(pick=True) )
	popular = Report.objects.filter(pub=True).order_by('views')
	page = request.GET.get('page', 1)
	paginator = Paginator(report, 10)
	try:
		report = paginator.page(page)
	except PageNotAnInteger:
		report = paginator.page(1)
	except EmptyPage:
		report = paginator.page(paginator.num_pages)
	context = {'report':report, 'picks':picks, 'popular':popular}
	return render(request, 'eyewitness/magazine/index.html', context)


# class EditorsPick(generic.ListView):
# 	models = Report
# 	paginate_by = 5
# 	template_name = 'eyewitness/magazine/editorpick.html'
# 	context_object_name = 'picks'

# 	def get_queryset(self):
# 		return Report.objects.filter(Q(pub=True) & Q(pick=True) ).order_by('date_pub')



class ReportListForAdmin(generic.ListView):
	models = Report
	paginate_by = 10
	template_name = 'eyewitness/magazine/allpost.html'
	context_object_name = 'reports'

	def get_queryset(self):
		return Report.objects.all().order_by('-date_pub')

def search(request):
	try:
		if request.method == 'GET':
			new_search = Report.objects.filter(Q(name__icontains = request.GET['q']) |
		 										Q(subject__icontains= request.GET['q']) |
		 										 Q(message__icontains = request.GET['q']) ).exclude(pub = False)
			search_name = request.GET['q']
		if new_search:
			context = {'new_search':new_search, 'search_name':search_name}
			return render(request, 'eyewitness/magazine/search.html', context)
		else:
			return render(request, 'eyewitness/magazine/search.html', {'search_name':search_name})

	except MultiValueDictKeyError as e:
		return render(request, 'rammyblog/404.html')


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
			url = full_report.get_absolute_url()
			print('hello', url)
			send_mail_submit(name,email,subject, url)
			messages.add_message(request, messages.INFO, 'Success! ')
			hello = redirect('details', full_report.slug)
			print(hello.url)
			print(full_report.get_absolute_url())
			return redirect('details', full_report.slug)
	else:
		form =ReportForm()
	context = {'form':form}
	return render(request, 'eyewitness/magazine/reportform.html', context)



def reportDetail(request, slug):
	report = get_object_or_404(Report, slug=slug)
	picks =  Report.objects.filter(Q(pub=True) & Q(pick=True))
	popular = Report.objects.filter(pub=True).order_by('views')
	comment = report.comments.all().order_by('-created_at')
	session_key = 'viewed_topic_{}'.format(report.slug)
	if not request.session.get(session_key, False):
		report.views+=1
		report.save()
		request.session[session_key] = True
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit = False)
			new_comment.report = report
			new_comment.save()
			return redirect('details', slug=slug)
	else:
		form = CommentForm()

	context = {'report':report, 'form':form, 'comment':comment, 'picks':picks, 'popular':popular}

	return render(request, 'eyewitness/magazine/detail.html', context)



def deleteComment(request, slug, comment_id):
	report = get_object_or_404(Report, slug=slug)
	comment = get_object_or_404(Comment, id=comment_id)
	if request.method == 'POST':
		comment.delete()
		return redirect('details', report.slug)
	context = {'comment':comment}
	return render(request, 'eyewitness/magazine/delete.html', context)




class DeleteDetail(generic.DeleteView):
	model = Report
	template_name = 'eyewitness/delete.html'
	context_object_name = 'report'
	success_url = 'all'


def publish_report(request, slug):
	report = get_object_or_404(Report, slug = slug)
	name = report.name
	message = report.message
	email= report.email
	subject = report.subject
	url = report.get_absolute_url()
	report.publish()
	send_mail_publish(name, email, subject, message, url)
	return redirect('details' , slug=slug)


def confirm_report(request, slug):
	report = get_object_or_404(Report, slug=slug)
	print(report.confrimed)
	session_key = 'viewed_topic_{}'.format(report.slug)
	if not request.session.get(session_key, False):
		report.confrimed+=1
		report.save()
		request.session[session_key] = True 	
	return redirect('details' , slug = slug)

def unconfirm_report(request, slug):
	report = get_object_or_404(Report, slug=slug)
	session_key = 'viewed_topic_{}'.format(report.slug)
	if not request.session.get(session_key, False):
		report.confrimed-=1
		report.save()
		request.session[session_key] = True 	
	return redirect('details' , slug = slug)









