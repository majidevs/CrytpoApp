from django.shortcuts import render
import requests
import json

def home(request):
	
	
	# Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,USDT,SOL,USDC,BNB,LINK,LTC,BUSD&tsyms=USD")
	price = json.loads(price_request.content)

	# Grab Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price': price})



def prices(request):
    if request.method == 'POST':

                quote = request.POST['quote']
                quote = quote.upper()
                crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
                crypto = json.loads(crypto_request.content)
                return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
            

    else:
        notfound = "Enter a valid crypto currency code.."
        return render(request, 'prices.html', {'notfound': notfound})
    

def news(request):
        api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
        api = json.loads(api_request.content)
        return render(request, 'news.html', {'api': api})



