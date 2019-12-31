import socket, message, ranger, math
import itertools as it

##### client configuration #####

SERVER_NAME = 'hostname'
SERVER_PORT = 3117
TEAM_NAME = 'TCP MONSTERS'
OFFER_TIMEOUT = 1000  # milliseconds
NUM_OF_LETTERS = 26


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hashed_string = input('Welcome to ' + TEAM_NAME + '.' + ' Please enter the hash:\n')
    length = input('Please enter the input string length:\n')
    test = divide(3,3)
    x=1
#    send_discover(client_socket)
#    client_socket.sendto(hashed_string,(server_name,server_port))


#def send_discover(socket):

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