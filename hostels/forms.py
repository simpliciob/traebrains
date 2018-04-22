from django import forms
from .models import Hostel

class HostelForm(forms.ModelForm):
    class Meta:
        
        model=Hostel
        fields=[
            'school',
            'student_number',
            'hostel_ID',
            'hostel_name',
             ]
    def __init__(self,user=None,*args,**kwargs):
        #print(kwargs.pop('user'))
        print(user)
        #print(kwargs.pop('instance'))
        super(HostelForm,self).__init__(*args,**kwargs)
         
    

                

