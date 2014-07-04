"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

import random
import ya_test
DICE_IN_GAME = 5

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set

    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    highest = 0
    for die in hand:
        temp = die * hand.count(die)
        if temp > highest:
            highest = temp

    return highest


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    remained_dice = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    possible_hand = set([tuple(list(held_dice) + list(pos_outcome)) for pos_outcome in remained_dice])

    temp_scores = []
    for hand in possible_hand:
        temp_scores.append(score(hand))

    return float(sum(temp_scores)) / len(temp_scores)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds_list = [[]]
    for die in hand:
        all_holds_list += [dummy_die + [die] for dummy_die in all_holds_list]

    all_holds = set([()])
    for single_hold in all_holds_list:
        all_holds.add(tuple(single_hold))

    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)

    best_strategy = (0.0 , ())
    for held_dice in all_holds:

        num_free_dice = len(hand) - len(held_dice)
        cur_expected_value = expected_value(held_dice, num_die_sides, num_free_dice)
        if cur_expected_value > best_strategy[0]:
            best_strategy = (cur_expected_value, held_dice)

    return best_strategy


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = [random.randrange(1, 7) for i in range(6)]
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


run_example()

# ya_test.test_score(score)

# ya_test.test_expected_value(expected_value)

# ya_test.test_gen_all_holds(gen_all_holds)

# ya_test.test_strategy(strategy)

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



