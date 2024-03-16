from django import forms
from .models import Variable

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = [
            'name',
            'first_name',
            'last_name',
            'document_type',
            'document_number',
            'date_of_birth',
            'city_of_residence',
            'email',
            'phone_number',
            'monthly_income',
        ]
        labels = {
            'name': 'Name',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'document_type': 'Document Type',
            'document_number': 'Document Number',
            'date_of_birth': 'Date of Birth',
            'city_of_residence': 'City of Residence',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'monthly_income': 'Monthly Income',
        }