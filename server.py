import socket
import message
import ranger
import encoder_decoder as encd
import hashlib
import threading

TEAM_NAME = 'UDP MONSTERS'
DISCOVER = '1'
OFFER = '2'
REQUEST = '3'
ACK = '4'
NEG_ACK = '5'
encoder_decoder: encd.Encoder_decoder = encd.Encoder_decoder()
server_port = 3101


class Server:
    server_socket = None

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(("", server_port))

    def search(self, start, end, hash_str):
        r: ranger.Ranger = ranger.Ranger(start, end)
        for word in r.generate_all_from_to_of_len():
            hash_fun_res = hashlib.sha1(word.encode('utf-8')).hexdigest()
            if hash_fun_res == hash_str:
                return word
        return None

    def process_message(self, user_message: message.Message, len):
        if user_message.type == DISCOVER:
                return encoder_decoder.encode(message.Message(user_message.team_name, OFFER, None, None, None, None))
        elif user_message.type == REQUEST:
            res = self.search(user_message.start[0:len], user_message.end[0:len], user_message.hash)
            if res is None:
                return encoder_decoder.encode(message.Message(TEAM_NAME, NEG_ACK, None, None, None, None))
            else:
                hash_msg = user_message.hash
                return encoder_decoder.encode(message.Message(TEAM_NAME, ACK,user_message.hash, None, res, None))

    def talkToClient(self, user_message:message.Message, ip):
        server_response = self.process_message(user_message, int(user_message.length))
        self.server_socket.sendto(server_response, ip)

    def listen_clients(self):
        print('server is running')
        while True:
            msg, client = self.server_socket.recvfrom(server_port)
            print("client connected, msg-" + encoder_decoder.decode(msg).type)
            decoded_msg =encoder_decoder.decode(msg)
            t = threading.Thread(target=self.talkToClient, args=(decoded_msg, client))
            t.start()


def main():
    server = Server()
    server.listen_clients()


if __name__ == "__main__":
    main()
