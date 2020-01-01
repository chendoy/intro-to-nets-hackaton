import message

TN_LEN = 32
TYPE_LEN = 1
HASH_LEN = 40
ORIG_LEN_LEN = 1
START_LEN = 256
END_LEN = 256

TN_OFFSET = 0
TYPE_OFFSET = 32
HASH_OFFSET = 33
ORIG_LEN_OFFSET = 73
START_OFFSET = 329
END_OFFSET = 585


def str_or_blank(_in):
    if _in is None:
        return ""
    else:
        return str(_in)


def len_or_blank(_in):
    if _in is None:
        return 0
    else:
        return len(_in)


class Encoder_decoder():
    pass


    def decode(self, encoded_msg):
        raw_str = encoded_msg.decode("utf-8")
        team_name = raw_str[TN_OFFSET:TN_OFFSET+TN_LEN]
        type = raw_str[TYPE_OFFSET:TYPE_OFFSET+TYPE_LEN]
        hash = raw_str[HASH_OFFSET:HASH_OFFSET+HASH_LEN]
        length = raw_str[ORIG_LEN_OFFSET:ORIG_LEN_OFFSET+ORIG_LEN_LEN]
        start = raw_str[START_OFFSET:START_OFFSET+START_LEN]
        end = raw_str[END_OFFSET:END_OFFSET+END_LEN]
        return message.Message(team_name, type, hash, length, start, end)

    def encode(self, message):
        orig_msg = ''
        padding = TN_LEN - len_or_blank(message.team_name)
        orig_msg += message.team_name + ('0' * padding)
        padding = TYPE_LEN - len_or_blank(message.type)
        orig_msg += str_or_blank(message.type) + ('0' * padding)
        padding = HASH_LEN - len_or_blank(message.hash)
        orig_msg += str_or_blank(message.hash) + ('0' * padding)
        padding = ORIG_LEN_LEN - len_or_blank(message.length)
        orig_msg += str_or_blank(message.length) + ('0' * padding)
        padding = START_LEN - len_or_blank(message.start)
        orig_msg += str_or_blank(message.start) + ('0' * padding)
        padding = END_LEN - len_or_blank(message.end)
        orig_msg += str_or_blank(message.end) + ('0' * padding)
        return bytes(orig_msg, 'utf-8')


