
from socket import *

DISCOVER = '1'
OFFER = '2'
REQUEST = '3'
ACK = '4'
NEG_ACK = '5'
TEAM_NAME = "somthing const"


def hash_func (str):
    return None

def scan_range(range_start, range_end, str_length, hash_message):

def send_offer():
    return HashMessage(TEAM_NAME, OFFER, None, None, None, None)


def proc_message(hash_msg: 'HashMessage'):

    if hash_msg.type == DISCOVER:
        send_offer()
    elif hash_msg.type == REQUEST:
        scan_range(hash_msg.orig_string_start, hash_msg.orig_sting_end, hash_msg.orig_length, hash_msg.message_hash)


def main():
    server_port = 3117
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("", server_port))
    while 1:
        message, client_address = server_socket.recvfrom(3117)
        server_socket.sendto(modified_message, client_address)




class HashMessage:
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


if __name__ == "__main__":
    main()