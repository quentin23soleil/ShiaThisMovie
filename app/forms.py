from django.forms import forms, IntegerField


class RateForm(forms.Form):
    rating = IntegerField()
    id = IntegerField()
