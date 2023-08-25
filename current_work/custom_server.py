import socket
import signal
import sys
import csv
import datetime
import netifaces

def get_wifi_ip():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        addresses = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addresses:
            for link in addresses[netifaces.AF_INET]:
                if 'addr' in link:
                    ip = link['addr']
                    if ip.startswith('192.168.79'):
                        return ip
    return None

def start_custom_server(port, password):
    # Get the local IP address
    ip = get_wifi_ip()

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define a signal handler to capture interrupt signal (Ctrl+C)
    def signal_handler(signal, frame):
        print("\nServer stopped.")
        server_socket.close()
        sys.exit(0)

    try:
        # Bind the socket to the local IP address and port
        server_socket.bind((ip, port))

        # Start listening for incoming connections
        server_socket.listen(1)
                

        # Register the signal handler for the interrupt signal (Ctrl+C)
        signal.signal(signal.SIGINT, signal_handler)

        while True:
            # Wait for a client to connect
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr[0]}:{addr[1]}")

            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr[0]}:{addr[1]}")
            
            # Get current timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Prompt user for nickname
            nickname = input("Please enter your nickname: ")
            
            # Write user data to CSV file
            with open("user_activity.csv", "a") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([timestamp, addr[0], addr[1], nickname])

            # Request password from the client
            client_socket.send("Please enter the password: ".encode())
            entered_password = client_socket.recv(1024).decode()

            # Check if the entered password is correct
            if entered_password == password:
                client_socket.send("Password accepted. Welcome!".encode())
                # Handle the client connection (you can implement your own logic here)
                # For example, you can receive data from the client:
                data = client_socket.recv(1024)
                print(f"Received data: {data.decode()}")
            else:
                client_socket.send("Incorrect password. Connection closed.".encode())
                # Close the client connection
                client_socket.close()

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        # Close the server socket
        server_socket.close()

    # After the server loop ends, return from the function
    return

def connect_to_server(ip, port, password):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((ip, port))
        print(f"Connected to server at {ip}:{port}")

        # Send the password to the server
        client_socket.send(password.encode())

        # Receive the server's response
        response = client_socket.recv(1024).decode()
        print(response)

        if "Password accepted" in response:
            # Handle client-server communication here
            # For example, you can send data to the server:
            data_to_send = "Hello from client!"
            client_socket.send(data_to_send.encode())

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        # Close the client socket
        client_socket.close()