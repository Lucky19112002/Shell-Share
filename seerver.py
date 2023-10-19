import http.server
import socketserver
import socket
import threading

# Global variables to indicate server and connection status
server_created = False
connection_established = False
server = None  # Store the server object

def create_server(port, password):
    """
    Create a basic HTTP server on the specified port.
    """
    global server_created, server
    if not server_created:
        try:
            Handler = http.server.SimpleHTTPRequestHandler
            server = socketserver.TCPServer(("", port), Handler)
            print(f"Server is running on port {port}")
            server_created = True
            server.serve_forever()
        except Exception as e:
            print(f"Error creating the server: {str(e)}")

def connect(ip, port, password):
    """
    Initiate a connection to another device and establish communication.
    """
    global server_created, connection_established, server

    if server_created:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip, port))
            print("Connected to remote device.")

            # Send the password
            client.send(password.encode())

            response = client.recv(1024).decode()
            if response == "Connection established":
                print("Connection established.")
                connection_established = True  # Set the flag to indicate successful connection
                # Implement listening for incoming requests here
            else:
                print("Connection failed. Incorrect password or error on the remote device.")
                connection_established = False  # Set the flag to indicate failed connection

            client.close()
        except Exception as e:
            print(f"Connection error: {str(e)}")
            connection_established = False  # Set the flag to indicate connection error
    else:
        print("Server has not been created. Sending a communication request to the remote device.")
        # Implement sending a communication request here
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip, port))
            print("Sending communication request to the remote device.")
            # Send your communication request data here
            # Example: client.send(b"Hello, this is a communication request.")
            client.close()
        except Exception as e:
            print(f"Error sending communication request: {str(e)}")
