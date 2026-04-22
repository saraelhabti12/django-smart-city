from django import forms
from .models import TrafficSignal

class TrafficSignalForm(forms.ModelForm):
    class Meta:
        model = TrafficSignal
        fields = ['intersection', 'state', 'cycle_duration', 'mode']
        widgets = {
            'intersection': forms.Select(attrs={'class': 'form-select'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'cycle_duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'mode': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_cycle_duration(self):
        cycle_duration = self.cleaned_data.get('cycle_duration')
        if cycle_duration is not None and cycle_duration <= 0:
            raise forms.ValidationError("Cycle duration must be a positive integer.")
        return cycle_duration