from django import forms
from .models import Vehicle, PriorityVehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['plate_number', 'vehicle_type', 'speed', 'status', 'current_road', 'battery_level', 'destination']
        widgets = {
            'plate_number': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-select'}),
            'speed': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'current_road': forms.Select(attrs={'class': 'form-select'}),
            'battery_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_speed(self):
        speed = self.cleaned_data.get('speed')
        if speed is not None and speed < 0:
            raise forms.ValidationError("Speed cannot be negative.")
        return speed

    def clean_battery_level(self):
        battery_level = self.cleaned_data.get('battery_level')
        if battery_level is not None:
            if battery_level < 0 or battery_level > 100:
                raise forms.ValidationError("Battery level must be between 0 and 100.")
        return battery_level

    def clean_plate_number(self):
        plate_number = self.cleaned_data.get('plate_number')
        if plate_number:
            query = Vehicle.objects.filter(plate_number=plate_number)
            if self.instance and self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
            if query.exists():
                raise forms.ValidationError("A vehicle with this plate number already exists.")
        return plate_number

class PriorityVehicleForm(forms.ModelForm):
    class Meta:
        model = PriorityVehicle
        fields = ['vehicle', 'mission', 'priority_level', 'progress', 'status']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-select'}),
            'mission': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_level': forms.Select(attrs={'class': 'form-select'}),
            'progress': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_progress(self):
        progress = self.cleaned_data.get('progress')
        if progress is not None:
            if progress < 0 or progress > 100:
                raise forms.ValidationError("Progress must be between 0 and 100.")
        return progress