class Message:
    def __init__(self,team_name):
        self.team_name = team_name
        self.type = None


class Discover(Message):
    def __init__(self,team_name):
        Message.__init__(self,team_name)
        self.type = 1


class Offer(Message):
    def __init__(self,team_name):
        Message.__init__(self,team_name)
        self.type = 2


class Request(Message):
    def __init__(self,team_name,hash,length,start,end):
        Message.__init__(self,team_name)
        self.type = 3
        self.hash = hash
        self.length = length
        self.start = start
        self.end = end


class Ack(Message):
    def __init__(self,team_name,hash,length,start):
        Message.__init__(self,team_name)
        self.type = 4
        self.hash = hash
        self.length = length
        self.start = start


class Nack(Message):
    def __init__(self,team_name,hash,length,start,end):
        Message.__init__(self,team_name)
        self.type = 5
        self.hash = hash
        self.length = length