import http.server
import socketserver
import socket
import threading
import time
import logging

# Global variables to indicate server and connection status
server_created = False
connection_established = False
server = None  # Store the server object
GREEN = "\033[92m"
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Received PUT request to update configuration")
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
            time.sleep(7)
            connected_msg = "Connected to 192.168.58.188"
            print(connected_msg)
            logging.info(connected_msg)
        except Exception as e:
            print(f"Error creating the server: {str(e)}")

def connect(IP,port,password):
    time.sleep(4)
    logging.info("Request from 192.168.58.188 on 4444")
    connected_msg = "Connected to 192.168.58.188"
    print(connected_msg)
    logging.info(connected_msg)
    print(GREEN + "> ExP - " + "\033[0m", end='', flush=True)
    time.sleep(5)
    print("Flag host by 192.168.58.188 - \"Bug in server\\var", end='', flush=True) 
    logging.info("Flag host by 192.168.58.188 - \"Bug in server\\var")
    print()
    