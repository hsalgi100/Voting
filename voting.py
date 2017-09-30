# Population voting

import random

"""
Variables: number_of_candidates -> int
           list_of_candidates   -> list of ints
           candidate_n          -> int
               ->  n will change for which candidate it is
           population_number    -> int (150 for now)
           voting_result        -> value in a dict (int)
           winner               -> int
"""


def voting_read(line):
    """
    read 2 ints
    line is a string
    :return: a list of 2 ints, representing the candidate and number of votes
    """
    # change this because I have no idea what I'm doing
    candidate, votes = line.split()
    candidate = int(candidate)
    votes = int(votes)
    return [candidate, votes]


# finds the candidate who has the most votes

def find_winner():
    # go through the dictionary of candidates and their number of votes (for loop)
    # find the candidate with the max number of votes (>= 50% of the population)
    # return that candidate (as an int)
    for key, value in candidates_and_votes.items():
        print(str(key) + ": " + str(value))
        if value >= 150//2:
            print(str(key))
            return key

    else:
        return "There is no solid majority. We need to have a re-vote."


candidates = [1, 2, 3, 4, 5]
candidates_and_votes = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}


def voting():
    # people is an int representing the number of people in a population
    # TODO: ASK
    people = 150
    while people > 0:
        # candidates is a list of the possible candidates
        # randomly puts the candidates in a list of a new order
        # TODO: figure out how to control order of a list multiple times
        random.shuffle(candidates)
        for key, value in candidates_and_votes.items():
            if candidates[0] == key:
                value += 1

    return candidates_and_votes


def voting_print(writer, winner, votes):
    """
    print 2 ints
    writer a writer
    *need another variable
    *possibly a second
    winner is the candidate with the most votes
    """
    writer.write(str(winner) + " " + str(votes) + " " + "\n")


def voting_solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        candidate, votes = voting_read(line)
        winner = find_winner()
        voting_print(writer, winner, votes)
