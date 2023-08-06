

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
            risk_tolerance = form.cleaned_data['risk_tolerance']
            time_horizon = form.cleaned_data['time_horizon']
            investment_amount = form.cleaned_data['investment_amount']
            emergency_fund_percentage = form.cleaned_data['emergency_fund_percentage']

            # Convert investment_amount to float
            investment_amount = float(investment_amount)

            # Calculate the allocation percentages based on user input
            stock_allocation = 0.5  # 50% for stocks
            mutual_fund_allocation = 0.2  # 20% for mutual funds
            emergency_fund_allocation = emergency_fund_percentage / 100  # Convert to decimal

            # Calculate investment amounts for each category
            stock_amount = stock_allocation * investment_amount
            mutual_fund_amount = mutual_fund_allocation * investment_amount
            emergency_fund_amount = emergency_fund_allocation * investment_amount

            # Fetch some example investment options (replace with your actual data)
            stocks = Stock.objects.all()[:5]
            mutual_funds = MutualFund.objects.all()[:5]

            return render(request, 'investment_strategy.html', {
                'stock_amount': stock_amount,
                'mutual_fund_amount': mutual_fund_amount,
                'emergency_fund_amount': emergency_fund_amount,
                'stocks': stocks,
                'mutual_funds': mutual_funds,
            })

    else:
        form = InvestmentForm()

    return render(request, 'investment_form.html', {'form': form})