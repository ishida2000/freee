from django.shortcuts import render, get_object_or_404
from .models import Employee, Attendance
from django.utils import timezone
import datetime
from datetime import timedelta

def check_in(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    Attendance.objects.create(employee=employee, check_in=timezone.now())
    return render(request, 'attendance/checked_in.html', {'employee': employee})

def check_out(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    attendance = Attendance.objects.filter(employee=employee).last()
    attendance.check_out = timezone.now()
    attendance.save()
    return render(request, 'attendance/checked_out.html', {'employee': employee})


def weekly_report(request, employee_id, year, week):
    employee = get_object_or_404(Employee, id=employee_id)
    date_min = datetime.datetime.strptime(f'{year}-W{int(week)-1}-1', "%Y-W%W-%w")
    date_max = date_min + timedelta(days=6.9)
    attendances = Attendance.objects.filter(employee=employee, check_in__range=[date_min, date_max])
    
    total_hours = sum([a.working_hours() for a in attendances])
    total_cost = sum([a.cost() for a in attendances])

    context = {
        'employee': employee,
        'total_hours': total_hours,
        'total_cost': total_cost,
        'year': year,
        'week': week,
    }

    return render(request, 'attendance/weekly_report.html', context)
