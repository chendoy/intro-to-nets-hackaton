import socket, message, ranger, math

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



if __name__ == "__main__":
    main()