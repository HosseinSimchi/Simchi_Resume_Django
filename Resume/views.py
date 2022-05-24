from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')
def portfolio_view(request):
    return render(request, 'portfolio-details.html')



