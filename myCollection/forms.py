from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

#here I'll create all my model form
class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            'name',
            'producer',
            'Type',
            'datepublish',
            'description',
            'photo'
        ]
        labels = {
            'name': 'Title',
            'producer': 'Producer/Sudio',
            'description':'Description',
            'datepublish': 'Date publish'
        }
        widgets = {
            'datepublish': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.fields['Type'].empty_label = "Choose..."
        self.fields['Type'].widget.attrs = {'class': 'form-select', 'id':"inputGroupSelect01"}
        self.fields['name'].widget.attrs = {'class': 'form-control', 'id':"first-name"}
        self.fields['producer'].widget.attrs = {'class': 'form-control', 'id':"first-name"}
        self.fields['description'].widget.attrs = {'class': 'form-control', 'id':"exampleFormControlTextarea", 'rows':"3" }
        self.fields['datepublish'].widget.attrs = {'class': 'form-control'}
        #self.fields['photo'].widget.attrs = {'class': 'form-file-input', 'id':"inputGroupFile01", 'aria-describedby':"inputGroupFileAddon01"}