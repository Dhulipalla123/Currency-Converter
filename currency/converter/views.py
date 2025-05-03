from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        from_currency = request.POST['from_currency']
        to_currency = request.POST['to_currency']
        amount = float(request.POST['amount'])

        # Get the exchange rate using an API (e.g. ExchangeRate-API or similar)
        api_key = '520d29d7ede95b9a0b06bba1'
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            conversion_result = data['conversion_result']
        else:
            conversion_result = 'Error: Invalid data received'

        context = {
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount,
            'conversion_result': conversion_result
        }
        return render(request, 'converter/index.html', context)

    return render(request, 'converter/index.html')


