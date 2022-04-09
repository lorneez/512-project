from Voter import Voter
from VotingProtocol import NormalVotingProtocol
import random
import math

class VotingEngine:
    def __init__(self, simulation_type):
        self.simulation_type = simulation_type

    def run(self):
        if self.simulation_type == "Normal-Test":
            self.run_test(0.0, 1000, "Normal", True)
        elif self.simulation_type == "Simulate-Normal-Test-100":
            self.simulate_normal_test(100, True)
        elif self.simulation_type == "Attacker-Test":
            self.run_test(0.3, 1000, "Normal", True)
            self.run_test(0.4, 1000, "Normal", True)
            self.run_test(0.5, 1000, "Normal", True)
            self.run_test(0.6, 1000, "Normal", True)
            self.run_test(0.7, 1000, "Normal", True)
        elif self.simulation_type == "Simulate-Attacker-Test-100":
            self.simulate_attacker_test(100, True)
    
    def simulate_attacker_test(self, rounds=100, verbose=False):
        if verbose: 
            print("Simulating Attacker Test 100 times...")
        pass_count = 0
        fail_count = 0
        tie_count = 0

        for p in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
            if verbose: 
                print("Attacker owns", 100 * p, "percent")
            for i in range(rounds):
                test_result = self.run_test(p, 1000, "Normal", False)
                if test_result == "PASS":
                    pass_count += 1
                elif test_result == "FAIL":
                    fail_count += 1
                else:
                    tie_count += 1
            if verbose:
                print("[pass, fail, tie] = ", [pass_count, fail_count, tie_count])
                print("Pass Percentage: ", 100 * pass_count / (pass_count + fail_count + tie_count))
                print("Fail Percentage: ", 100 * fail_count / (pass_count + fail_count + tie_count))
                print("Tie Percentage: ", 100 * tie_count / (pass_count + fail_count + tie_count))

    def simulate_normal_test(self, rounds=100, verbose=False):
        if verbose: 
            print("Simulating Normal Test 100 times...")
        pass_count = 0
        fail_count = 0
        tie_count = 0

        for i in range(rounds):
            test_result = self.run_test(0.0, 1000, "Normal", False)
            if test_result == "PASS":
                pass_count += 1
            elif test_result == "FAIL":
                fail_count += 1
            else:
                tie_count += 1
        if verbose:
            print("[pass, fail, tie] = ", [pass_count, fail_count, tie_count])
            print("Pass Percentage: ", 100 * pass_count / (pass_count + fail_count + tie_count))
            print("Fail Percentage: ", 100 * fail_count / (pass_count + fail_count + tie_count))
            print("Tie Percentage: ", 100 * tie_count / (pass_count + fail_count + tie_count))

    def run_test(self, attacker_stake, num_votes, voting_protocol, verbose=False):
        if verbose: 
            print("Running Normal Test...")
        no_count = 0
        yes_count = 0

        if attacker_stake != 0.0 and verbose:
            print("Attacker owns", attacker_stake * 100, "percent")

        voters = []
        attacker_votes = math.floor(num_votes * attacker_stake)
        normal_votes = num_votes - attacker_votes
        # attacker votes
        for i in range(attacker_votes):
            voters.append(Voter("Bad-Yes"))
            yes_count += 1
        # normal votes
        for i in range(normal_votes):
            chance = random.randint(0, 1)
            if chance:
                voters.append(Voter("Normal-Yes"))
                yes_count += 1
            else:
                voters.append(Voter("Normal-No"))
                no_count += 1
        if verbose:
            print("[yes, no] = ", [yes_count, no_count])

        votes = []
        for voter in voters:
            votes.append(voter.getVotes())

        if voting_protocol == "Normal":
            protocol = NormalVotingProtocol(votes)
        elif voting_protocol == "Quadratic":
            protocol = QuadraticVotingProtocol(votes)

        result = protocol.process()
        if verbose:
            print("Result: ", result)
        return result


engine = VotingEngine("Normal-Test")
engine.run()

engine = VotingEngine("Simulate-Normal-Test-100")
engine.run()

engine = VotingEngine("Attacker-Test")
engine.run()

engine = VotingEngine("Simulate-Attacker-Test-100")
engine.run()