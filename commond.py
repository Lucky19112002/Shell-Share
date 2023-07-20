import sys
import os
import time
import random
import pyfiglet
import socket
import multiprocessing
from current_work import dummy

# ANSI escape sequence for green color
GREEN = "\033[92m"

def connect(args):
    if len(args) != 2:
        print("\tInvalid command. Usage: connect [IP] [PORT]")
        return
    ip, port = args
    print(f"\tConnected to {ip}:{port}")
    print(f"\tIP: {ip}")
    print(f"\tPort: {port}")

def create(args):
    if len(args) != 2:
        print("\tInvalid command. Usage: create [port] [password]")
        return
    port, password = args
    ip = socket.gethostbyname(socket.gethostname())
    print(f"\tFetching user IP address...")
    print(f"\tUser IP address: {ip}")
    print(f"\tPort: {port}")
    print(f"\tPassword: {password}", end="")  # Output on the same line without a new line

    # Convert port to integer
    ports = int(port)

    # Start the custom server as a separate process
    server_process = multiprocessing.Process(target=dummy.start_custom_server, args=(ports, password))

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
    # Add your logic here to fetch and print the list of connected users

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
    art = pyfiglet.Figlet(font=random.choice(pyfiglet.Figlet().getFonts()))
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



