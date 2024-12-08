n = int(input())
prices = [int(input()) for _ in range(n)]

min_price = prices[0]
profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    profit = max(profit, price - min_price)

if profit > 0:
    print("Profit:", profit)
else:
    print("Meera never bought, as prices are going down..")
