from django.shortcuts import render
from django.db.models import F
from .models import MainDataSet, SelectedData
from django.db.models import Q


# Create your views here.


def index(request):
    # Get risk tolerance from GET parameter (using the correct name)
    user_risk_tolerance = request.GET.get('demo-category', '')
    
    # Filter schemes where returns_1yr < returns_3yr < returns_5yr
    filtered_schemes2 = SelectedData.objects.filter(
        returns_1yr__lt=F('returns_3yr'),
        returns_3yr__lt=F('returns_5yr')
    )
    # For higher risk tolerance, recommend funds with highest 5yr returns 
    highest_5yr_returns = filtered_schemes2.order_by('-returns_5yr')[:6]

    # For lower risk tolerance, recommend funds with lowest 5yr returns
    lowest_5yr_returns = filtered_schemes2.order_by('returns_5yr')[:6]
    
    # Select the top 5 based on 5-year returns (descending order)
    top_5_schemes = filtered_schemes2.order_by('-returns_5yr')[:5]
    if not user_risk_tolerance:
        # Handle case where risk tolerance is not provided
        context = {
        "top_5_schemes": top_5_schemes,
        "highest_5yr_returns": highest_5yr_returns,
        "lowest_5yr_returns": lowest_5yr_returns,
        }
        template_name = "index.html"
        return render(request, template_name, context=context) 

    filtered_schemes = SelectedData.objects.all()  # All schemes initially

    if user_risk_tolerance == "high":
        sorted_schemes = filtered_schemes.order_by('-returns_5yr')[:6]  # Top 5 with highest 5yr returns
    else:
        sorted_schemes = filtered_schemes.order_by('returns_5yr')[:6]  

    recommended_funds = [scheme.scheme_name for scheme in sorted_schemes]

    

    context = {
        "top_5_schemes": top_5_schemes,
        "recommended_funds": recommended_funds,
        "highest_5yr_returns": highest_5yr_returns,
        "lowest_5yr_returns": lowest_5yr_returns,
    }


    template_name = "index.html"
    return render(request, template_name, context=context)


def consistent_returns(request):
    search_query = request.GET.get('search', '')
    print(search_query)

    filtered_schemes = SelectedData.objects.filter(
        returns_1yr__lt=F('returns_3yr'),
        returns_3yr__lt=F('returns_5yr')
    )

    if search_query:
        search_filters = Q(scheme_name__icontains=search_query) | \
                         Q(risk_category__icontains=search_query) | \
                         Q(risk_level__icontains=search_query) | \
                         Q(returns_5yr__icontains=search_query) | \
                         Q(returns_3yr__icontains=search_query) | \
                         Q(returns_1yr__icontains=search_query)
        filtered_schemes = filtered_schemes.filter(search_filters)

        print(filtered_schemes)

    context = {
        "filtered_schemes": filtered_schemes,
    }
    template_name = "consistentFunds.html"
    return render(request, template_name, context=context)

def learn_more(request):
    template_name = "generic.html"
    return render(request, template_name)