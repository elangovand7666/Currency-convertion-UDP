from socket import *
def re(amount,f,t):
    serverName = '192.168.146.82'  # Replace with the server's IP address
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    while True:
        message=str(amount+' '+f+' '+t)
        
        if message.lower() == 'exit':
            print("Exiting the currency converter.")
            break
        
        print("Sending message to server...")
        clientSocket.sendto(message.encode(), (serverName, serverPort)) 
        
        try:
            response, serverAddress = clientSocket.recvfrom(2048)
            print("Received response from server:", response.decode())
            return str(response.decode())
        except timeout:
            print("Request timed out.")
            return ('timeout')
    clientSocket.close()
