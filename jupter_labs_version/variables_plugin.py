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
def question_ask():
    while True:
        # Ask the user for a stock ticker symbol
        ticker = input("Enter a stock ticker symbol: ").upper()
        # Call the get_stock_name function to get the full name of the stock
        stock_name = get_stock_name(ticker)
        # If a valid full name was returned, proceed with the rest of the program
        if stock_name and ticker != 'SPY':
            # Print the full name of the stock
            print(f"The name of the stock is: {stock_name}")
            
            # ask how long they would like to hold the security for
            while True:
                hold_unit = input("Would you like to hold this for security for (days, months, years): ").lower()
                if hold_unit in ["days", "months", "years"]:
                    break
                else:
                    print("Invalid input. Please enter either 'days', 'months', or 'years'.")
             
            # Continuously ask the user for the holding time (in number) until a valid numeric input is entered
            while True:
                try:
                    hold_time = int(input(f"How many {hold_unit} would you like to hold the security for? "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            # Continuously ask the user for the holding time unit (days, months, years) until a valid input is entered
            
            while True:
                try:
                    req_return = float(input(f"What is your annualized required rate of return for this investment? (Enter as a Percentage. Example: 5.3 returns 5.3%)"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            # Continuously ask the user for the required rate of return

            print(f"You want to hold the {ticker} for {hold_time} {hold_unit} and you are looking for a {req_return}% return.")
        # If an invalid full name was returned, print an error message and loop back to the beginning
        else:
            print("Invalid stock ticker or you have selected SPY. Please enter another ticker.")
            continue
        # Ask the user if they want to proceed
        proceed = input("Do you want to proceed? (yes/no): ")
        # If the user does not want to proceed, break out of the main loop
        if (proceed.lower() == "yes") or (proceed.lower() == "y"):
            break
    return ticker, hold_time, hold_unit, req_return
