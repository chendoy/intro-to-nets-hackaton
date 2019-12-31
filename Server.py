from
from socket import *

class HashMessage :
    team_name = None
    message_type = None
    message_hash = None
    orig_length = None
    orig_string_start = None
    orig_sting_end = None
    def __init__(self, team_name, message_type, message_hash, orig_length, orig_string_start, orig_sting_end):
        self.team_name =team_name
        self.type = type
        self.hash = hash
        self.message_type = message_type
        self.message_hash = message_hash
        self.orig_length = orig_length
        self.orig_string_start = orig_string_start
        self.orig_sting_end = orig_sting_end




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