
# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')




from django.shortcuts import render
from .forms import InvestmentForm
from .models import Stock, MutualFund

def investment_strategy(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            # Get the form data and process it
            risk_tolerance = form.cleaned_data['risk_tolerance']
            time_horizon = form.cleaned_data['time_horizon']
            investment_amount = form.cleaned_data['investment_amount']
            emergency_fund_percentage = form.cleaned_data['emergency_fund_percentage']

            # Convert investment_amount to float
            investment_amount = float(investment_amount)

            # Calculate the allocation percentages based on user input
            stock_allocation = get_stock_allocation(risk_tolerance, time_horizon)
            mutual_fund_allocation = get_mutual_fund_allocation(risk_tolerance, time_horizon)
            emergency_fund_allocation = emergency_fund_percentage / 100  # Convert to decimal

            # Calculate investment amounts for each category
            stock_amount = stock_allocation * investment_amount
            mutual_fund_amount = mutual_fund_allocation * investment_amount
            emergency_fund_amount = emergency_fund_allocation * investment_amount

            # Replace this with your actual SIP suggestion logic
            suggested_sips = [
                {'name': 'SIP Option 1', 'type': 'Equity', 'amount': 100},
                {'name': 'SIP Option 2', 'type': 'Debt', 'amount': 150}
            ]

            return render(request, 'investment_strategy.html', {
                'stock_amount': stock_amount,
                'mutual_fund_amount': mutual_fund_amount,
                'emergency_fund_amount': emergency_fund_amount,
                'suggested_sips': suggested_sips,
            })

    else:
        form = InvestmentForm()

    return render(request, 'services.html', {'form': form})

def get_stock_allocation(risk_tolerance, time_horizon):
    # Calculate stock allocation based on risk tolerance and time horizon
    if risk_tolerance == '1':
        return 0.4 if time_horizon == '3' else 0.3
    elif risk_tolerance == '2':
        return 0.5 if time_horizon == '3' else 0.4
    else:
        return 0.6 if time_horizon == '3' else 0.5

def get_mutual_fund_allocation(risk_tolerance, time_horizon):
    # Calculate mutual fund allocation based on risk tolerance and time horizon
    if risk_tolerance == '1':
        return 0.3 if time_horizon == '3' else 0.4
    elif risk_tolerance == '2':
        return 0.3 if time_horizon == '3' else 0.3
    else:
        return 0.2 if time_horizon == '3' else 0.2