from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = '__all__'
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Enter weight in lbs'}),
        }

    def __init__(self, *args, **kwargs):
        super(QuoteRequestForm, self).__init__(*args, **kwargs)
        self.fields['broker_name'].widget.attrs.update({'placeholder': 'Broker Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['pickup'].widget.attrs.update({'placeholder': 'Pickup Location'})
        self.fields['dropoff'].widget.attrs.update({'placeholder': 'Dropoff Location'})
        self.fields['equipment'].widget.attrs.update({'placeholder': 'Select Equipment'})
        self.fields['weight'].widget.attrs.update({'placeholder': 'Enter weight in lbs'})
        self.fields['pickup_date'].widget.attrs.update({'placeholder': 'Select Pickup Date'})
        self.fields['notes'].widget.attrs.update({'placeholder': 'Any special requirements,handling instructions, or additional details..'})


