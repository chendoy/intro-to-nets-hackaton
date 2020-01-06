import socket
import message
import string_utils
import encoder_decoder as encd
import hashlib
import threading

TEAM_NAME = 'UDP FTW'
DISCOVER = 1
OFFER = 2
REQUEST = 3
ACK = 4
NEG_ACK = 5
encoder_decoder: encd.Encoder_decoder = encd.Encoder_decoder()
server_port = 3117


class Server:
    server_socket = None

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(("", server_port))

    def search(self, start, end, hash_str):
        r: string_utils.Ranger = string_utils.Ranger(start, end)
        for word in r.generate_all_from_to_of_len():
            hash_fun_res = hashlib.sha1(word.encode('utf-8')).hexdigest()
            if hash_fun_res == hash_str:
                return word
        return ""

    def process_message(self, user_message: message.Message, len):
        if user_message.type == DISCOVER:
                self.echo_msg_info(OFFER)
                return encoder_decoder.encode(message.Message(user_message.team_name, OFFER, "", 1, "", ""))
        elif user_message.type == REQUEST:
            res = self.search(user_message.start[0:len], user_message.end[0:len], user_message.hash)
            if res is "":
                self.echo_msg_info(NEG_ACK)
                return encoder_decoder.encode(message.Message(TEAM_NAME, NEG_ACK, "", len, "", ""))
            else:
                hash_msg = user_message.hash
                self.echo_msg_info(ACK)
                return encoder_decoder.encode(message.Message(TEAM_NAME, ACK,hash_msg, len, res, ""))

    def talkToClient(self, user_message:message.Message, ip):
        server_response = self.process_message(user_message, user_message.length)
        self.server_socket.sendto(server_response, ip)


    def echo_msg_info(self, type):
        if type == 1:
            print('received: discover')
        elif type == 2:
            print('sent: offer')
        elif type == 3:
            print('received: request')
        elif type == 4:
            print('sent: ack')
        elif type == 5:
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
