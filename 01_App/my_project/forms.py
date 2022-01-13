from .models import DataView
from django.forms import ModelForm, TextInput

class DataViewForm(ModelForm):
    class Meta:
        model = DataView
        fields = ['data']
        widgets = {'data': TextInput(attrs={
            'class': 'form-control',
            'name': 'data',
            'id': 'data',
            'placeholder': 'Input Date. Pattern  YYYY-MM-DD '
        })}

