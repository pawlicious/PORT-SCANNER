import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(7)
host =input("Enter the IP that you want to scan:")
port = int(input("Enter the Port number:"))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)



