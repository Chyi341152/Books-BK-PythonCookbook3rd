# Calculating with Dictionaries
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(prices.keys(), prices.values())
# zip() creates an items  that can only be consumed once s
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)