import requests
import sys

try:
    n = float(sys.argv[1])
except (IndexError, ValueError) as e:
    print(f"command-line error: {e}")
    sys.exit(1)

try:
    response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

data = response.json()
result = n * data["bpi"]["USD"]["rate_float"]
print(f"${result:,.4f}")

