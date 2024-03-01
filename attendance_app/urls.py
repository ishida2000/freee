from django.urls import path
from . import views

urlpatterns = [
    path('check_in/<int:employee_id>/', views.check_in, name='check_in'),
    path('check_out/<int:employee_id>/', views.check_out, name='check_out'),
    path('report/<int:employee_id>/<int:year>/<int:week>/', views.weekly_report, name='weekly_report'),
]