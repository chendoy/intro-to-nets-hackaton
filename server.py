import socket
import message
import ranger
import encoder_decoder as encd
import hashlib
import threading

TEAM_NAME = 'UDP FTW'
DISCOVER = '1'
OFFER = '2'
REQUEST = '3'
ACK = '4'
NEG_ACK = '5'
encoder_decoder: encd.Encoder_decoder = encd.Encoder_decoder()
server_port = 3117


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
                self.echo_msg_info(OFFER)
                return encoder_decoder.encode(message.Message(user_message.team_name, OFFER, None, None, None, None))
        elif user_message.type == REQUEST:
            res = self.search(user_message.start[0:len], user_message.end[0:len], user_message.hash)
            if res is None:
                self.echo_msg_info(NEG_ACK)
                return encoder_decoder.encode(message.Message(TEAM_NAME, NEG_ACK, None, str(len), None, None))
            else:
                hash_msg = user_message.hash
                self.echo_msg_info(ACK)
                return encoder_decoder.encode(message.Message(TEAM_NAME, ACK,hash_msg, str(len), res, None))

    def talkToClient(self, user_message:message.Message, ip):
        server_response = self.process_message(user_message, int(user_message.length))
        self.server_socket.sendto(server_response, ip)


    def echo_msg_info(self, type):
        if type is '1':
            print('received: discover')
        elif type is '2':
            print('sent: offer')
        elif type is '3':
            print('received: request')
        elif type is '4':
            print('sent: ack')
        elif type is '5':
            print('sent: nack')
        return

    def listen_clients(self):
        print('server is running...')
        while True:
            msg, client = self.server_socket.recvfrom(server_port)
            decoded_msg =encoder_decoder.decode(msg)
            self.echo_msg_info(decoded_msg.type)
            t = threading.Thread(target=self.talkToClient, args=(decoded_msg, client))
            t.start()


def main():
    server = Server()
    server.listen_clients()


if __name__ == "__main__":
    main()
