import requests

r = requests.get("https://www.financialmodelingprep.com/api/v3/historical-chart/1min/AAPL?apikey=demo")

print(r.text)



# reference = https://www.financialmodelingprep.com/api/v3/historical-chart/1min/AAPL?apikey=demo