from django import forms

class InvestmentForm(forms.Form):
    risk_tolerance = forms.ChoiceField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    time_horizon = forms.ChoiceField(choices=[(1, 'Short-term'), (2, 'Medium-term'), (3, 'Long-term')])
    investment_amount = forms.DecimalField(max_digits=10, decimal_places=2)
    emergency_fund_percentage = forms.IntegerField(min_value=0, max_value=100)