import requests
import locale

def get_exchange_rate(base_currency, target_currency):
    """Returns the exchange rate between two currencies."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][target_currency]
    return exchange_rate

def exchange_currency(amount, base_currency, target_currency):
    """Converts an amount from one currency to another."""
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

# Set the locale to the user's default locale
locale.setlocale(locale.LC_ALL, "")

# Define a dictionary of currency codes and symbols
currencies = {
    "USD": "$",
    "COP": "COL$",
    "EUR": "€",
    "JPY": "¥",
    "KRW": "₩"
}

while True:
    # Prompt the user to enter the amount to exchange
    amount = float(input("Enter the amount to exchange: "))

    # Prompt the user to select the base currency
    print("Select a base currency:")
    for i, currency in enumerate(currencies):
        print(f"{i+1}. {currency} ({currencies[currency]})")
    base_choice = int(input("Enter the number of your choice: "))
    base_currency = list(currencies.keys())[base_choice-1]

    # Prompt the user to select the target currency
    print("Select a target currency:")
    for i, currency in enumerate(currencies):
        print(f"{i+1}. {currency} ({currencies[currency]})")
    target_choice = int(input("Enter the number of your choice: "))
    target_currency = list(currencies.keys())[target_choice-1]

    # Convert the amount from the base currency to the target currency
    target_amount = exchange_currency(amount, base_currency, target_currency)

    # Format the target amount with the appropriate decimal separator and currency symbol
    formatted_amount = locale.currency(target_amount, grouping=True, symbol=currencies[target_currency])

    print(f"{amount:.2f} {base_currency} is equal to {formatted_amount} {target_currency}")

    # Ask the user if they want to exchange another amount
    choice = input("Do you want to exchange another amount? (Y/N): ")
    if choice.lower() == "n":
        break
