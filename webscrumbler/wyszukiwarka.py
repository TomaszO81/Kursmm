import requests

response = requests.get('http://trojmiasto.pl/')
print(response.status_code)

try:
    response.raise_for_status()
except Exception as e:
    print('Błąd:', e)

