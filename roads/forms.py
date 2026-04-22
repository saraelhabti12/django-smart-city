from django import forms
from .models import Road

class RoadForm(forms.ModelForm):
    class Meta:
        model = Road
        fields = ['name', 'zone', 'speed_limit', 'direction', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'zone': forms.TextInput(attrs={'class': 'form-control'}),
            'speed_limit': forms.NumberInput(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_speed_limit(self):
        speed_limit = self.cleaned_data.get('speed_limit')
        if speed_limit is not None and speed_limit < 0:
            raise forms.ValidationError("Speed limit cannot be negative.")
        return speed_limit