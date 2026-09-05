# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("===================================")
print("       STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Ask how many different stocks the user wants to enter
number_of_stocks = int(input("\nHow many stocks do you want to add? "))

portfolio = []

# Get stock information from the user
for i in range(number_of_stocks):

    print(f"\n--- Stock {i + 1} ---")

    stock_name = input("Enter stock name: ").upper()

    # Check if stock exists
    if stock_name not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]

    investment = price * quantity

    total_investment += investment

    # Store information
    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print(f"Price per share: ${price}")
    print(f"Investment in {stock_name}: ${investment}")


# Display portfolio summary
print("\n===================================")
print("         PORTFOLIO SUMMARY")
print("===================================")

for item in portfolio:
    print(
        f"{item['stock']} | "
        f"Quantity: {item['quantity']} | "
        f"Price: ${item['price']} | "
        f"Value: ${item['investment']}"
    )

print("-----------------------------------")
print(f"Total Investment: ${total_investment}")
print("===================================")


# Save result to a text file
save_result = input("\nDo you want to save the result? (yes/no): ").lower()

if save_result == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=======================\n\n")

        for item in portfolio:
            file.write(
                f"Stock: {item['stock']}\n"
                f"Quantity: {item['quantity']}\n"
                f"Price: ${item['price']}\n"
                f"Investment: ${item['investment']}\n\n"
            )

        file.write("-----------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Portfolio saved successfully to portfolio.txt")

else:
    print("Result was not saved.")