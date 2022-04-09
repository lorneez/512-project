from Vote import Vote

class Voter:

    def __init__(self, voter_type):
        self.voter_type = voter_type
        if self.voter_type == "Normal-Yes":
            self.vote = Vote(1,1)
        elif self.voter_type == "Normal-No":
            self.vote = Vote(-1,1)
        elif self.voter_type == "Bad-Yes":
            self.vote = Vote(1,1)
        elif self.voter_type == "Bad-No":
            self.vote = Vote(-1,1)

    def getType(self):
        return self.voter_type

    def getVotes(self):
        return self.vote