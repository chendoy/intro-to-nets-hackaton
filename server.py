from socket import *

def scan_range(rnage):


def get_range(message):

def send_offer():


def proc_message(message):
    if message == "DISCOVER":
        send_offer()
    elif message == "REQUEST":
        scan_range(get_range(message))


def main():
    server_port = 3117
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("", server_port))
    while 1:
        message, client_address = server_socket.recvfrom(3117)

        server_socket.sendto(modified_message, client_address)

if _name_ == '_main_':
    main()