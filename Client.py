from socket import *

server_name = 'hostname'
server_port = 3117
team_name = 'TCP MONSTERS'

def main():
    client_socket = socket(socket.AF_INET, socket.SOCK_DGRAM)
    hashed_string = input('Welcome to ' + team_name + '.' + ' Please enter the hash:\n')
    length = input('Please enter the input string length:\n')
    #discover()
#    client_socket.sendto(hashed_string,(server_name,server_port))


#def discover():



if __name__ == "__main__":
    main()