"""
Test suite for expected_value in "Yahtzee"
"""

import poc_simpletest

def test_score(score):
    """
    Some informal testing code for score
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test score on various inputs
    hand = tuple([])
    suite.run_test(score(hand), 0, "Test #1:")

    hand = tuple([4, 2])
    suite.run_test(score(hand), 4, "Test #2:")

    hand = tuple((1, 2, 2))
    suite.run_test(score(hand), 4, "Test #3:")

    hand = tuple((2, 1, 2))
    suite.run_test(score(hand), 4, "Test #4:")

    hand = tuple([6, 2, 3])
    suite.run_test(score(hand), 6, "Test #5:")

    suite.report_results()

def test_expected_value(expected_value):
    """
    Some informal testing code for gen_all_holds
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test expected_value on various inputs
    held_dice =  ()
    num_die_sides = 6
    num_free_dice = 2
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(5.0555556, 7), "Test #1:")


    held_dice =  (2, 1, 2)
    num_die_sides = 6
    num_free_dice = 3
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(6.9120370, 7), "Test #2:")


    held_dice =  (2,)
    num_die_sides = 6
    num_free_dice = 5
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(8.8801440, 7), "Test #3:")


    held_dice =  (1,)
    num_die_sides = 6
    num_free_dice = 2
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(5.0833333, 7), "Test #4:")


    held_dice =  (2, 1)
    num_die_sides = 6
    num_free_dice = 3
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(6.4722222, 7), "Test #5:")


    held_dice =  (2, 2)
    num_die_sides = 6
    num_free_dice = 5
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(9.2250514, 7), "Test #6:")


    held_dice =  (1, 2)
    num_die_sides = 6
    num_free_dice = 4
    suite.run_test(round(expected_value(held_dice, num_die_sides, num_free_dice), 7), round(7.6689815, 7), "Test #7:")


    suite.report_results()


def test_gen_all_holds(gen_all_holds):
    """
    Some informal testing code for gen_all_holds
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test gen_all_holds on various inputs
    hand = tuple([])
    suite.run_test(gen_all_holds(hand), set([()]), "Test #1:")

    hand = tuple([4, 2])
    suite.run_test(gen_all_holds(hand), set([(), (4,), (2,), (4, 2)]), "Test #2:")

    hand = tuple((1, 2, 2))
    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #3:")

    hand = tuple((2, 1, 2))
    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 1), (2, 2), (2, 1, 2)]), "Test #4:")

    hand = tuple([6, 2, 3])
    suite.run_test(gen_all_holds(hand),set([(), (6,), (2,), (6, 2), (3,), (6, 3), (2, 3), (6, 2, 3)]), "Test #5:")

    suite.report_results()


def test_strategy(strategy):
    """
    Some informal testing code for strategy
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test strategy on various inputs
    num_die_sides =  5
    hand =  (1, 3, 5, 3, 3)
    suite.run_test(strategy(hand, num_die_sides), (10.24, (3, 3, 3)), "Test #1:")


    num_die_sides =  4
    hand =  (3, 3, 3, 3)
    suite.run_test(strategy(hand, num_die_sides), (12.0, (3, 3, 3, 3)), "Test #2:")


    num_die_sides =  4
    hand =  (3, 1, 4, 4, 4)
    suite.run_test(strategy(hand, num_die_sides), (14.0, (4, 4, 4)), "Test #3:")


    num_die_sides =  8
    hand =  (1, 8, 4, 8)
    suite.run_test(strategy(hand, num_die_sides), (18.0, (8, 8)), "Test #4:")


    num_die_sides =  4
    hand =  (3, 1, 1, 3, 2)
    suite.run_test(strategy(hand, num_die_sides), (8.53125, (3, 3)), "Test #5:")


    num_die_sides =  6
    hand =  (6, 5)
    suite.run_test(strategy(hand, num_die_sides), (7.0, (6,)), "Test #6:")


    num_die_sides =  8
    hand =  (1, 8, 8)
    suite.run_test(strategy(hand, num_die_sides), (17.0, (8, 8)), "Test #7:")


    suite.report_results()
