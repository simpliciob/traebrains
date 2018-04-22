from django import forms
from .models import Fee

class   FeesForm(forms.ModelForm):
    class Meta:
        
        model=Fee
        fields=[
            'school',
            'student_number',
            'Amount_paid',
            'invoice_number',
            'tutoring_fee',
            'Bank_name',
             ]
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(FeesForm,self).__init__(*args,**kwargs)
         
    

                

