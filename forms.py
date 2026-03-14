from django import forms
from .models import Scan

class Scanform(forms.ModelForm):
    class Meta:

        model = Scan

        fields = ["patient_name","image"]
        
        labels ={
            "patient_name":"Enter you Name",
            "image":"Upload Xray/Scan Image"
        }

        widgets = {
            'patient_name':forms.TextInput(attrs={
                'placeholder':'Enter Your Name',
                'class':'Medical-input'
            }),
            'image':forms.FileInput(attrs={
                'class':'Image-input',
                'accept':'image/*'
            })
        }