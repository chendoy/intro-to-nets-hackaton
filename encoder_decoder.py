import message as message

class Encoder_decoder():
    pass

    def decode(self, encoded_msg):
        return encoded_msg.decode("utf-8")

    def encode(self, orig_msg):
        orig_msg = ''
        orig_msg += message.team_name
        orig_msg += message.type
        orig_msg += message.hash
        orig_msg += message.length
        orig_msg += message.start
        orig_msg += message.end
        return bytes(orig_msg, 'utf-8')