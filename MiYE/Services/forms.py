from django import forms
from .models import Services, Options

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('types', 'options','Price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['options'].queryset = Options.objects.none()

        if 'Types' in self.data:
            try:
                types_id = int(self.data.get('Types'))
                self.fields['Options'].queryset = Options.objects.filter(types_id=types_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Options'].queryset = self.instance.types.options_set.order_by('name')
