
class Vote:
    def __init__(self, vote, cost):
        self.vote = vote
        self.cost = cost

    def getVote(self):
        return self.vote

    def getCost(self):
        return self.cost
    
    def getVoteCount(self):
        return self.vote * self.cost
