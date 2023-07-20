import sys
sys.path.append("current_work")

import dummy

port = 5000  # Specify the desired port number
password = input("Enter the password for the server: ")  # Prompt the user to enter the password
dummy.start_custom_server(port, password)
