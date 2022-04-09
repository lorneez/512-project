
class VotingProtocol:
    vote_result = 0
    
    def __init__(self, votes):
        self.votes = votes

class NormalVotingProtocol(VotingProtocol):
    def process(self):
        for vote in self.votes:
            vote_count = vote.getVoteCount()
            self.vote_result += vote_count
        
        if self.vote_result > 0:
            return "PASS"
        elif self.vote_result < 0:
            return "FAIL"
        else:
            return "TIE"

    
class QuadraticVotingProtocol(VotingProtocol):
    def process(self):
        for vote in self.votes:
            vote_count = vote.getVoteCount()
            vote_weight = (vote_count**2)/2
            self.vote_result += vote_weight
        
        if self.vote_result > 0:
            return "PASS"
        elif self.vote_result < 0:
            return "FAIL"
        else:
            return "TIE"