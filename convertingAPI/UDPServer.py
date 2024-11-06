from socket import *
import requests
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
api_key = "efe58e93482bd2ff3837bc64"
api_url = "https://api.exchangerate-api.com/v4/latest/"

print('Currency Converter Server is ready to receive requests.')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)# Receive the message from the client
    print("Received request:", message.decode())# Print the received request
    data = message.decode().split()# Process the received message
    if len(data) != 3:
        response = "Invalid Format!"
    else:
        try:
            amount = float(data[0])
            from_currency = data[1].upper()
            to_currency = data[2].upper()
            #API to fetch conversion data
            response_api = requests.get(f"{api_url}{from_currency}", params={"apikey": api_key})
            if response_api.status_code == 200:
                exchange_rates = response_api.json().get("rates")
                if to_currency in exchange_rates:
                    rate = exchange_rates[to_currency]
                    converted_amount = amount * rate
                    response = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
                else:
                    response = f"Error: Unable to convert to {to_currency}."
            else:
                response = "Error: Failed to retrieve exchange rates."
        except Exception as e:
            response = f"Error: {str(e)}" 
    serverSocket.sendto(response.encode(), clientAddress)#Sending the response back
