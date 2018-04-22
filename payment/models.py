from django.db import models
class Payment(models.Model):
    school=models.CharField(max_length=50)
    Amount_paid=models.DecimalField(max_digits=5, decimal_places=2)
    student_number=models.CharField(max_length=50)
    invoice_number=models.CharField(max_length=50)
    tutoring_fee=models.DecimalField(max_digits=5, decimal_places=2)
    Bank_name=models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('fpayment:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('payment:update', kwargs={'pk':self.pk})
    

# Create your models here.
