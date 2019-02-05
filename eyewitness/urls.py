from django.urls import path
from . import  views

urlpatterns = [
	path('create/', views.reportForm_, name='create'),
    # path('', views.ReportList.as_view(), name='all'),
    path('', views.index, name='all'),  
    #path('editors/pick/', views.EditorsPick.as_view(), name='pick'),
    path('allposts/', views.ReportListForAdmin.as_view(), name='allposts'),
    path('publish/<slug>/', views.publish_report, name='publish'),
    path('search/', views.search, name='search'),
    path('confirm/<slug>', views.confirm_report, name='confirm'),
    path('unconfirm/<slug>', views.unconfirm_report, name='unconfirm'),
    # path('create/', views.CreateReport.as_view(), name='create'),
    path('detail/<slug>/', views.reportDetail, name='details'),
    path('delete/<slug>/', views.DeleteDetail.as_view(), name='delete'),
    path('delete/<slug>/<comment_id>', views.deleteComment, name='delete'),
]
