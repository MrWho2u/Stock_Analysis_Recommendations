import requests

# Define a function that takes in a stock ticker symbol and returns its full name
def get_stock_name(ticker):
    # Create a URL using the ticker symbol
    endpoint = "https://finance.yahoo.com/quote/" + ticker
    # Send a GET request to the URL
    response = requests.get(endpoint)
    # If the response status code is 200 (success), extract the full name of the stock
    if response.status_code == 200:
        start_index = response.text.find('<title>') + len('<title>')
        end_index = response.text.find('</title>')
        full_name = response.text[start_index:end_index].split("(")[0].strip()
        return full_name
    # If the response status code is not 200 (failure), return None
    else:
        return None

# Continuously ask the user for a stock ticker symbol until they choose to stop
def question_ask(ticker):
    stock_name = get_stock_name(ticker)
    # If a valid full name was returned, proceed with the rest of the program
    if stock_name and ticker != 'SPY':
        # Print the full name of the stock
        stock_confirm = f"{stock_name}"
    else:
        stock_confirm = "invalid stock ticker or you have selected SPY. Please enter another ticker."
    return stock_confirm
