from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q
User=settings.AUTH_USER_MODEL
class Hostel(models.Model):
    user=models.ForeignKey(User)
    school=models.CharField(max_length=50)
    hostel_ID=models.CharField(max_length=20)
    hostel_name=models.CharField(max_length=20)
    student_number=models.CharField(max_length=50)
    def __str__(self):
        return self.hostel_ID
    def get_absolute_url(self):
        return reverse('hoste:detail', kwargs={'pk':self.pk})
    def get_absolute_url(self):
        return reverse('hoste:update', kwargs={'pk':self.pk}) 


# Create your models here.

