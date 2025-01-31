import unittest
import server
import message as msg
import encoder_decoder as encd
import time

TEAM_NAME = 'UDP FTW'
DISCOVER = b'1'
OFFER = b'2'
REQUEST = b'3'
ACK = b'4'
NACK = b'5'


class Tester(unittest.TestCase):
    server_side: server.Server = server.Server()
    encoder_decoder: encd.Encoder_decoder = encd.Encoder_decoder()

    def test_searching(self):
        res = self.server_side.search("aaa", "zzz", "99875401d16283b911c70b1ddbc25ac40836367f", time.time())
        self.assertEqual(res, "tst")
        res = self.server_side.search("aaazzcs", "zzzzzza", "1f8ac10f23c5b5bc1167bda84b833e5c057a77d2", time.time())
        self.assertEqual(res, "abcdef")

    def test_processMessage(self):
        # discover message Message
        discover_msg: msg.Message = msg.Message(TEAM_NAME, DISCOVER, None, None, None, None)
        res = self.server_side.process_message(discover_msg)
        res_message: msg.Message = self.encoder_decoder.decode(res)
        self.assertEqual(res_message.type, OFFER)

        #request, with ack
        request_msg: msg.Message = msg.Message(TEAM_NAME, REQUEST, "12abf551138756adc2a88edc23cb77b1832b7ab8", '3', 'aaa', 'ccc')
        res = self.server_side.process_message(request_msg)
        res_message: msg.Message = self.encoder_decoder.decode(res)
        self.assertEqual(res_message.type, ACK)

        #request with nack
        request_msg: msg.Message = msg.Message(TEAM_NAME, REQUEST, "12abf551138756adc2a88edc23cb77b1832b7ab8", '3', 'aad', 'ccc')
        res = self.server_side.process_message(request_msg)
        res_message: msg.Message = self.encoder_decoder.decode(res)
        self.assertEqual(res_message.type, NACK)
