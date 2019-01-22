from django.urls import path
from . import  views

urlpatterns = [
	path('create/', views.reportForm_, name='create'),
    path('', views.ReportList.as_view(), name='all'),
    path('allposts/', views.ReportListForAdmin.as_view(), name='allposts'),
    path('publish/<slug>/', views.publish_report, name='publish'),
    # path('create/', views.CreateReport.as_view(), name='create'),
    path('detail/<slug>/', views.ReportDetail.as_view(), name='details'),
    path('delete/<slug>/', views.DeleteDetail.as_view(), name='delete')
]
