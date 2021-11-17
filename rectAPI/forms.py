from django import forms

from rectAPI.models import order

class OrderForm(forms.ModelForm):
    first_name= forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    totalcost = forms.FloatField()
    note = forms.CharField(max_length=100)

    class Meta:
        model = order

        fields = ['first_name', 'last_name', 'totalcost','note']