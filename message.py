class Message:
    def __init__(self,team_name, type, hash, length, start, end):
        self.team_name = team_name
        self.type = type
        self.hash = hash
        self.length = length
        self.start = start
        self.end = end