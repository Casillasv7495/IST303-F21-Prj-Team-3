from django import forms
from .models import Reservations, Customer


class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name','email','phone','membership')

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields[''].queryset = Options.objects.none()

    #    if 'types' in self.data:
    #        try:
    #            types_id = int(self.data.get('types'))
    #            self.fields['options'].queryset = Options.objects.filter(types_id=types_id).order_by('name')
    #        except (ValueError, TypeError):
    #            pass  # invalid input from the client; ignore and fallback to empty City queryset
    #    elif self.instance.pk:
    #        self.fields['options'].queryset = self.instance.types.options_set.order_by('name')
