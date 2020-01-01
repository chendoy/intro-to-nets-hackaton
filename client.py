import socket, ranger, math, encoder_decoder, select
import itertools as it
import message as message

# client configuration #

SERVER_NAME = 'hostname'
SERVER_PORT = 3117
TEAM_NAME = 'TCP MONSTERS'
OFFER_TIMEOUT = 1000  # milliseconds
NUM_OF_LETTERS = 26
IP_ADDRESS = '127.0.0.1'
WORKERS = []


def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    enc_dec = encoder_decoder.Encoder_decoder()
    hashed_string = input('Welcome to ' + TEAM_NAME + '.' + ' Please enter the hash:\n')
    length = input('Please enter the input string length:\n')
    send_discover(client_sock, enc_dec)
    wait_for_offers(client_sock, enc_dec, OFFER_TIMEOUT)
#    client_socket.sendto(hashed_string,(server_name,server_port))


def send_discover(client_socket: socket, enc_dec: encoder_decoder):
    discover_msg = message.Message(TEAM_NAME, message.DISCOVER, None, None, None, None)
    encoded = enc_dec.encode(discover_msg)
    client_socket.sendto(encoded, (SERVER_NAME, SERVER_PORT))

def wait_for_offers(client_sock, enc_dec, timeout):
    client_sock.setblocking(0)
    client_sock.settimeout(OFFER_TIMEOUT)
    while(1):
        (msg, server_address) = client_sock.recvfrom(2048)
        WORKERS.append(server_address)

def split_to_chunks(lst, each):
    return list(it.zip_longest(*[iter(lst)] * each))


def divide(length,num_servers):
    start = 'a' * length
    end   = 'z' * length
    search_space = ranger.Ranger(start,end)
    num_strings = NUM_OF_LETTERS ** length
    strings = search_space.generate_all_from_to_of_len()
    each = math.ceil(num_strings / num_servers)
    chunks = split_to_chunks(strings,each)
    return chunks


if __name__ == "__main__":
    main()