#https://chat.openai.com/share/ccfdb74c-d31a-486a-adfc-f48cb34ad920
# change code that contain csv that input user data when they connected to network and store their details

import socket
import signal
import sys
import csv
import random
import string
import logging
import sqlite3

def generate_random_number():
    # Generate a random number for the user
    return random.randint(1000, 9999)

def setup_logging():
    # Configure the logging module to generate log files
    logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def create_database_table():
    # Connect to the database (if it doesn't exist, it will be created)
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Create the "users" table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY,
                      ip TEXT,
                      nickname TEXT,
                      random_number INTEGER
                      )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def start_custom_server(port, password):
    # Get the local IP address
    ip = socket.gethostbyname(socket.gethostname())

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

        setup_logging()
        logging.info(f"Server is up and running on {ip}:{port}")

        while True:
            # Wait for a client to connect
            client_socket, addr = server_socket.accept()

            # Request password from the client
            client_socket.send("Please enter the password: ".encode())
            entered_password = client_socket.recv(1024).decode()

            # Check if the entered password is correct
            if entered_password == password:
                client_socket.send("Password accepted. Welcome!".encode())

                # Ask the client to enter a nickname
                client_socket.send("Please enter your nickname: ".encode())
                nickname = client_socket.recv(1024).decode()

                # Generate a random number for the user
                random_number = generate_random_number()

                # Store user data in the database
                conn = sqlite3.connect('user_data.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (ip, nickname, random_number) VALUES (?, ?, ?)", (addr[0], nickname, random_number))
                conn.commit()
                conn.close()

                # Handle the client connection (you can implement your own logic here)
                # For example, you can receive data from the client:
                data = client_socket.recv(1024)
                print(f"Received data: {data.decode()}")

                # Log the successful connection in the log file
                logging.info(f"Connected to {addr[0]}:{addr[1]} - Nickname: {nickname}, Random Number: {random_number}")

            else:
                client_socket.send("Incorrect password. Connection closed.".encode())
                # Close the client connection
                client_socket.close()

    except ConnectionAbortedError:
        logging.warning("Connection was abruptly closed by the client.")
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

    finally:
        # Close the server socket
        server_socket.close()

    # After the server loop ends, return from the function
    return

# Call the function to create the database and table
create_database_table()

# Call the function to start the server
port = 5000  # Specify the desired port number
password = input("Enter the password for the server: ")  # Prompt the user to enter the password
start_custom_server(port, password)
