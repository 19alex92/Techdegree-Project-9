from django import forms
from django.forms.widgets import SelectDateWidget

from .models import Menu


class MenuForm(forms.ModelForm):

    expiration_date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Menu
        fields = ['season', 'items', 'expiration_date']

    def clean_items(self):
        items = self.cleaned_data['items']
        count = 0
        for _ in items:
            count += 1
        if count <= 1:
            raise forms.ValidationError("Choose at least two items for the menu")
        return items

    def clean_season(self):
        season = self.cleaned_data['season']
        if len(season) < 4:
            raise forms.ValidationError("The season name must at least be 4 characters long")
        return season
