from django.db import models
from django.utils import timezone
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0.00) 


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    
    def working_hours(self):
        if self.check_out:
            return (self.check_out - self.check_in).total_seconds() / 3600.0  
        return 0

    def cost(self):
        return self.working_hours() * self.employee.hourly_rate
