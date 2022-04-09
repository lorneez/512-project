
class Vote:
    def __init__(self, vote, weight):
        self.vote = vote
        self.weight = weight

    def getVote(self):
        return self.vote

    def getWeight(self):
        return self.weight
    
    def getVoteCount(self):
        return self.vote * self.weight
