from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
User=settings.AUTH_USER_MODEL
class Fee(models.Model):
    user=models.ForeignKey(User)
    school=models.CharField(max_length=50)
    Amount_paid=models.DecimalField(max_digits=5, decimal_places=2)
    student_number=models.CharField(max_length=50)
    invoice_number=models.CharField(max_length=50)
    tutoring_fee=models.DecimalField(max_digits=5, decimal_places=2)
    Bank_name=models.CharField(max_length=50)
    def __str__(self):
        return self.student_number
    def get_absolute_url(self):
        return reverse('fees:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('fees:update', kwargs={'pk':self.pk}) 



# Create your models here.
