import sys
import os
import time
import random
import pyfiglet
import socket,csv
import multiprocessing
from current_work import custom_server
import netifaces

# ANSI escape sequence for green color
GREEN = "\033[92m"

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
def connect(args):
    if len(args) != 2:
        print("\tInvalid command. Usage: connect [IP] [PORT]")
        return
    ip, port = args
    print(f"\tConnecting to {ip}:{port}")
    password = input("Please enter the password: ")  # Prompt user for password
     
    # Start the connection process in a separate background process
    connection_process = multiprocessing.Process(target=custom_server.connect_to_server, args=(ip, int(port), password))
    
    # Set the process as a daemon so that it runs in the background and terminates when the main program ends
    connection_process.daemon = True
    
    # Start the process
    connection_process.start()
    
    # Wait for a short period to check if the connection process is still alive
    time.sleep(2)
    
    if connection_process.is_alive():
        print(f"\tConnected to {ip}:{port}")
    else:
        print(f"\tConnection failed. Please check for any errors.")

def create(args):
    if len(args) != 2:
        print("\tInvalid command. Usage: create [port] [password]")
        return
    port, password = args
    ip = get_wifi_ip()
    print(f"\tFetching user IP address...")
    print(f"\tUser IP address: {ip}")
    print(f"\tPort: {port}")
    print(f"\tPassword: {password}", end="")  # Output on the same line without a new line

    # Convert port to integer
    ports = int(port)

    # Start the custom server as a separate process
    server_process = multiprocessing.Process(target=custom_server.start_custom_server, args=(ports, password))

    # Set the process as a daemon so that it runs in the background and terminates when the main program ends
    server_process.daemon = True

    # Start the process
    server_process.start()
    print()  # Move to the next line after printing password without a new line

    # Wait for a short period to check if the server process is still alive
    time.sleep(2)

    if server_process.is_alive():
        print(f"\tServer is up and running on {ip}:{ports}")
    else:
        print(f"\tServer failed to start. Please check for any errors.")



def log(args):
    filename = args[0]
    print(f"\tLogging to file: {filename}")

def shell(args):
    print("\tList of connected users:")
    
    # Read and display the CSV file
    with open("current_work/user_activity.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            print(f"\tTimestamp: {row[0]}, IP Address: {row[1]}, Port: {row[2]}, Nickname: {row[3]}")

def help():
    print("Available commands:")
    print("\tconnect [IP] [PORT]: Connect to a server with the given IP and PORT.\n")
    print("\tcreate [port] [password]: Create a user with the specified port and password.\n")
    print("\tlog [filename]: Print the specified file name.\n")
    print("\tshell: Print the list of users currently connected to the local server.\n")
    print("\thelp: Display this help message.\n")
    print("\texit: Exit the program.\n")

def rambo_exit_animation():
    text = "Exiting..."
    delay = 0.1
    colors = [random.choice(range(91, 97)) for _ in text]  # Generate random colors for each character
    spaces = " " * len(text)

    for _ in range(3):
        for i in range(len(text)):
            colored_char = f"\033[{colors[i]}m{text[i]}\033[0m"
            print(spaces[:i] + colored_char + text[i+1:] + spaces[i+1:], end="\r", flush=True)
            time.sleep(delay)
        for i in reversed(range(len(text))):
            colored_char = f"\033[{colors[i]}m{text[i]}\033[0m"
            print(spaces[:i] + colored_char + text[i+1:] + spaces[i+1:], end="\r", flush=True)
            time.sleep(delay)

def main():
    font_styles = [
        'xttyb', 'xsansb', 'xhelv', 'xcour', 'utopiai', 'univers', 'unarmed_', 'ucf_fan_','type_set', 'ttyb', '1943____', '3x5', '4x4_offr', '5lineoblique', '5x7', '6x10','6x9', 'advenger', 'aquaplan', 'ascii___', 'asc_____', 'assalt_m', 'asslt__m','atc_gran', 'banner', 'banner3', 'basic', 'beer_pub', 'big', 'bubble_b', 'c1______','char1___', 'char3___', 'clb6x10', 'coil_cop', 'com_sen_', 'demo_m__', 'digital','doom', 'drpepper', 'epic', 'etcrvs__', 'funky_dr', 'future_7', 'fuzzy', 'helv','helvi', 'hyper___', 'italic', 'kik_star', 'lcd', 'mig_ally', 'mcg_____', 'new_asci','ok_beer_', 'puffy', 'p_skateb', 'rad_____', 'rectangles', 'rok_____', 'sansb','sansbi', 'sbook', 'sbookb', 'sbooki', 'sbookbi', 'skateord', 'slant', 'straight','super_te', 'taxi____', 'times', 'tomahawk'
        ]
    art = pyfiglet.Figlet(font=random.choice(font_styles))
    print(GREEN + art.renderText("SHELL SHARE") + "\033[0m")
    print(GREEN + "Welcome to Shell Share CLI" + "\033[0m")
    print(GREEN + "Version 1.0.0" + "\033[0m")
    print(GREEN + "Type 'help' to see available commands.\n" + "\033[0m")

    while True:
        command = input(GREEN + "> ExP - " + "\033[0m").strip().lower()
        parts = command.split()

        if parts[0] == "connect":
            if len(parts) != 3:
                print("\tInvalid command. Usage: connect [IP] [PORT]")
                continue
            connect(parts[1:])
        elif parts[0] == "create":
            if len(parts) != 3:
                print("\tInvalid command. Usage: create [port] [password]")
                continue
            create(parts[1:])
        elif parts[0] == "log":
            if len(parts) != 2:
                print("\tInvalid command. Usage: log [filename]")
                continue
            log(parts[1:])
        elif parts[0] == "shell":
            if len(parts) != 1:
                print("\tInvalid command. Usage: shell")
                continue
            shell(parts[1:])
        elif parts[0] == "help":
            if len(parts) != 1:
                print("\tInvalid command. Usage: help")
                continue
            help()
        elif parts[0] == "exit":
            if len(parts) != 1:
                print("\tInvalid command. Usage: exit")
                continue
            rambo_exit_animation()# Delay of 3 seconds
            sys.exit()  # Exit the program
        else:
            print("\tUnknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()



