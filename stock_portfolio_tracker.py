# CodeAlpha Python Programming Internship
# Task 2 - Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock}: {quantity} shares × "
              f"${stock_prices[stock]} = ${investment}")

    except ValueError:
        print("Please enter a valid number.")

print("\n================================")
print(f"Total Investment: ${total_investment}")
print("================================")

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("=======================\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("Result saved to portfolio.txt")