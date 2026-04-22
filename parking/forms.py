from django import forms
from .models import Parking

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ['name', 'capacity', 'occupied_places', 'price', 'charging_station']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'occupied_places': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'charging_station': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_capacity(self):
        capacity = self.cleaned_data.get('capacity')
        if capacity is not None and capacity < 0:
            raise forms.ValidationError("Capacity cannot be negative.")
        return capacity

    def clean_occupied_places(self):
        occupied_places = self.cleaned_data.get('occupied_places')
        if occupied_places is not None and occupied_places < 0:
            raise forms.ValidationError("Occupied places cannot be negative.")
        return occupied_places

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    def clean(self):
        cleaned_data = super().clean()
        capacity = cleaned_data.get('capacity')
        occupied_places = cleaned_data.get('occupied_places')

        if capacity is not None and occupied_places is not None:
            if occupied_places > capacity:
                raise forms.ValidationError(
                    {"occupied_places": "Occupied places cannot exceed total capacity."}
                )
        return cleaned_data