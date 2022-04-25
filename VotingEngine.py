from Voter import Voter
from VotingProtocol import *
import random
import math

class VotingEngine:
    def __init__(self, simulation_type):
        self.simulation_type = simulation_type

    def run(self):
        if self.simulation_type == "Normal-Test":
            self.run_test(0.0, 1000, "Normal", True, True)
        elif self.simulation_type == "Simulate-Normal-Test-100":
            self.simulate_normal_test(100, True)
        elif self.simulation_type == "Attacker-Test":
            self.run_test(0.1, 1000, "Normal", True, True)
        elif self.simulation_type == "Sybil-Attacker-Quadratic-Test":
            self.run_test(0.1, 1000, "Quadratic", True)
        elif self.simulation_type == "Sybil-Attacker-PQV-Test":
            self.run_test(0.1, 1000, "PQV", True)
        elif self.simulation_type == "Simulate-Attacker-Test-100":
            print("Protocol: Normal, Attacker: No Partition")
            self.simulate_attacker_test(100, "Normal", False, True, 0.1)
        elif self.simulation_type == "Simulate-Sybil-Attacker-Quadratic-Test-100":
            print("Protocol: Normal, Attacker: Partition")
            self.simulate_attacker_test(100, "Quadratic", False, True, 0.1)
        elif self.simulation_type == "Simulate-Sybil-Attacker-PQV-Test-100":
            print("Protocol: Quadratic, Attacker: No Partition")
            self.simulate_attacker_test(100, "PQV", False, True, 0.1)
        elif self.simulation_type == "Simulate-Attacker-Test-100-P":
            print("Protocol: Quadratic, Attacker: Partition")
            self.simulate_attacker_test(100, "Normal", True, True, 0.1)
        elif self.simulation_type == "Simulate-Sybil-Attacker-Quadratic-Test-100-P":
            print("Protocol: PQV, Attacker: No Partition")
            self.simulate_attacker_test(100, "Quadratic", True, True, 0.1)
        elif self.simulation_type == "Simulate-Sybil-Attacker-PQV-Test-100-P":
            print("Protocol: PQV, Attacker: Partition")
            self.simulate_attacker_test(100, "PQV", True, True, 0.1)
        elif self.simulation_type == "Simulate-PQV-Partition-10":
            print("Protocol: PQV, Attacker: Partition")
            self.simulate_attacker_test(100, "PQV", True, True, 0.1)
        elif self.simulation_type == "Simulate-PQV-Partition-20":
            print("Protocol: PQV, Attacker: Partition")
            self.simulate_attacker_test(100, "PQV", True, True, 0.2)
        elif self.simulation_type == "Simulate-PQV-Partition-30":
            print("Protocol: PQV, Attacker: Partition")
            self.simulate_attacker_test(100, "PQV", True, True, 0.3)
        elif self.simulation_type == "Simulate-Quadratic-Partition-10":
            print("Protocol: Quadratic, Attacker: Partition")
            self.simulate_attacker_test(100, "Quadratic", True, True, 0.1)
        elif self.simulation_type == "Simulate-Quadratic-Partition-20":
            print("Protocol: Quadratic, Attacker: Partition")
            self.simulate_attacker_test(100, "Quadratic", True, True, 0.2)
        elif self.simulation_type == "Simulate-Quadratic-Partition-30":
            print("Protocol: Quadratic, Attacker: Partition")
            self.simulate_attacker_test(100, "Quadratic", True, True, 0.3)
        elif self.simulation_type == "Simulate-Quadratic-Partition-Increasing-Percentage":
            print("Protocol: Quadratic, Attacker: Partition")
            for p in range(0,31):
                percent = p/100
                self.simulate_attacker_test(100, "Quadratic", True, True, percent)
        elif self.simulation_type == "Simulate-PQV-Partition-Increasing-Percentage":
            print("Protocol: PQV, Attacker: Partition")
            for p in range(0,101):
                percent = p/100
                self.simulate_attacker_test(100, "PQV", True, True, percent)
            
    
    def simulate_attacker_test(self, rounds=100, attacker_type="Normal", partition=False, verbose=False, attacker_percent=0.1):
        # if verbose: 
        #     print("Simulating Attacker Test 100 times...")
        pass_count = 0
        fail_count = 0
        tie_count = 0

        if verbose: 
            print("Attacker owns", 100 * attacker_percent, "percent")
        for i in range(rounds):
            test_result = self.run_test(attacker_percent, 1000, attacker_type, partition, False)
            if test_result == "PASS":
                pass_count += 1
            elif test_result == "FAIL":
                fail_count += 1
            else:
                tie_count += 1
        if verbose:
            print("[pass, fail, tie] = ", [pass_count, fail_count, tie_count])
            # print("Pass Percentage: ", 100 * pass_count / (pass_count + fail_count + tie_count))
            # print("Fail Percentage: ", 100 * fail_count / (pass_count + fail_count + tie_count))
            # print("Tie Percentage: ", 100 * tie_count / (pass_count + fail_count + tie_count))
            

    def simulate_normal_test(self, rounds=100, verbose=False):
        if verbose: 
            print("Simulating Normal Test 100 times...")
        pass_count = 0
        fail_count = 0
        tie_count = 0

        for i in range(rounds):
            test_result = self.run_test(0.0, 1000, "Normal", True, False)
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

    def run_test(self, attacker_stake, num_votes, voting_protocol, partition, verbose=False):
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
        if voting_protocol == "PQV" or voting_protocol == "Quadratic" and not partition:
            sybil_voter = Voter("Sybil-100-Yes")
            voters.append(sybil_voter)
            yes_count += 100
        else:
            for i in range(attacker_votes):
                voters.append(Voter("Sybil-1-Yes"))
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
        elif voting_protocol == "PQV":
            protocol = ProbabilisticQuadraticVotingProtocol(votes)

        result = protocol.process()
        if verbose:
            print("Result: ", result)
        return result

###### INITIAL TESTS
# engine = VotingEngine("Normal-Test")
# engine.run()

# engine = VotingEngine("Simulate-Normal-Test-100")
# engine.run()

# engine = VotingEngine("Attacker-Test")
# engine.run()

# engine = VotingEngine("Simulate-Attacker-Test-100")
# engine.run()

###### ATTACK SIMULATIONS: Changing Voting Protocol
# engine = VotingEngine("Simulate-Attacker-Test-100")
# engine.run()
# engine = VotingEngine("Simulate-Attacker-Test-100-P")
# engine.run()

# engine = VotingEngine("Simulate-Sybil-Attacker-Quadratic-Test-100")
# engine.run()
# engine = VotingEngine("Simulate-Sybil-Attacker-Quadratic-Test-100-P")
# engine.run()

# engine = VotingEngine("Simulate-Sybil-Attacker-PQV-Test-100")
# engine.run()
# engine = VotingEngine("Simulate-Sybil-Attacker-PQV-Test-100-P")
# engine.run()

###### ATTACK SIMULATIONS: Increasing Attacker Percentage
# engine = VotingEngine("Simulate-Quadratic-Partition-10")
# engine.run()
# engine = VotingEngine("Simulate-Quadratic-Partition-20")
# engine.run()
# engine = VotingEngine("Simulate-Quadratic-Partition-30")
# engine.run()

# engine = VotingEngine("Simulate-PQV-Partition-10")
# engine.run()
# engine = VotingEngine("Simulate-PQV-Partition-20")
# engine.run()
# engine = VotingEngine("Simulate-PQV-Partition-30")
# engine.run()

engine = VotingEngine("Simulate-Quadratic-Partition-Increasing-Percentage")
engine.run()
engine = VotingEngine("Simulate-PQV-Partition-Increasing-Percentage")
engine.run()