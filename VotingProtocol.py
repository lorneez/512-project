import math
import random

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
            vote_count = vote.getCost()
            vote_weight = math.sqrt(vote_count)
            self.vote_result += vote_weight * vote.getVote()
        
        if self.vote_result > 0:
            return "PASS"
        elif self.vote_result < 0:
            return "FAIL"
        else:
            return "TIE"

class ProbabilisticQuadraticVotingProtocol(VotingProtocol):
    def process(self):
        num_total_votes = 0
        for vote in self.votes:
            num_total_votes += vote.getCost()

        for vote in self.votes:
            vote_count = vote.getCost()
            success_probability = (vote_count/num_total_votes)
            if random.random() > success_probability:
                vote_weight = 0
            else:
                vote_weight = (math.sqrt(vote_count))
            
            
            self.vote_result += vote_weight * vote.getVote()
        
        if self.vote_result > 0:
            return "PASS"
        elif self.vote_result < 0:
            return "FAIL"
        else:
            return "TIE"