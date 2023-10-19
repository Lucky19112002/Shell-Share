import sys
import time
import random
import pyfiglet
from seerver import create_server, connect

# ANSI escape sequence for green color
GREEN = "\033[92m"

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
            ip, port = parts[1:]
            password = input("Please enter the password: ")
            connect(ip, int(port), password)  # Convert port to an integer
        elif parts[0] == "create":
            if len(parts) != 3:
                print("\tInvalid command. Usage: create [port] [password]")
                continue
            port, password = parts[1:]
            create_server(int(port), password)  # Convert port to an integer

        elif parts[0] == "help":
            if len(parts) != 1:
                print("\tInvalid command. Usage: help")
                continue
            help()
        elif parts[0] == "exit":
            if len(parts) != 1:
                print("\tInvalid command. Usage: exit")
                continue
            rambo_exit_animation()
            sys.exit()
        else:
            print("\tUnknown command. Type 'help' to see available commands.")

def help():
    print("Available commands:")
    print("\tconnect [IP] [PORT]: Connect to a server with the given IP and PORT.\n")
    print("\tcreate [port] [password]: Create a user with the specified port and password.\n")
    print("\thelp: Display this help message.\n")
    print("\texit: Exit the program.\n")

def rambo_exit_animation():
    text = "Exiting..."
    delay = 0.1
    colors = [random.choice(range(91, 97)) for _ in text]
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

if __name__ == "__main__":
    main()
