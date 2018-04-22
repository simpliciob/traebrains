from django import forms
from .models import Payment

class   PaymentForm(forms.ModelForm):
    class Meta:
        
        model=Payment
        fields=[
            'student_number',
            'Amound_paid',
            'invoice_number',
            'tutoring_fee',
            'Bank_name',
             ]
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(PaymentForm,self).__init__(*args,**kwargs)
         
    

                

