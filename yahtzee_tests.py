from yahtzee import *

def test_gen_all_sequences():
    assert gen_all_sequences(set([0, 1, 2, 3]), 2) == set([(0, 1), (1, 2), (3, 2), (0, 0), (3, 3), (3, 0), (3, 1), (2, 1), (1, 1), (2, 0), (1, 3), (2, 3), (2, 2), (1, 0), (0, 3), (0, 2)])
