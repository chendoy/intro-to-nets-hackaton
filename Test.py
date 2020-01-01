import unittest
import server
import message as msg
import encoder_decoder as encd

TEAM_NAME = 'kapara'
DISCOVER = '1'
OFFER = '2'
REQUEST = '3'
ACK = '4'
NACK = '5'


class Tester(unittest.TestCase):
    server_side: server.Server = server.Server()
    encoder_decoder: encd.Encoder_decoder = encd.Encoder_decoder()

    def test_searching(self):
        res = self.server_side.search("aaa", "zzz", "99875401d16283b911c70b1ddbc25ac40836367f")
        self.assertEqual(res, "tst")

        res = self.server_side.search("aaazzcs", "zzzzzza", "01cf32fce06fa4139787a54c3b6af902ae113ade")
        self.assertEqual(res, "aacjhnb")

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
