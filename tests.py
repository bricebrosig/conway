""" test.py

test suite for conway's game of life
"""

from conway import *
from typing import List

def test_advance() -> List:
    failures = []

    print("single cell : ", end="")
    if len(advance({(1, 1)})) == 0: 
        print("OK")
    else: 
        print("FAILED")
        failures.append("Test 1: single cell")

    print("square still life : ", end="")
    if advance({(0, 0), (0, 1), (1, 0), (1, 1)}) == {(0, 0), (0, 1), (1, 0), (1, 1)}:
        print("OK")
    else:
        print("FAILED")
        failures.append("Test 2: square still life")

    print("almost square -> still life : ", end="")
    if advance({(0, 0), (0, 1), (1, 0)}) == {(0, 0), (0, 1), (1, 0), (1, 1)}:
        print("OK")
    else:
        print("FAILED")
        failures.append("Test 3: almost square -> still life")

    print("reproduction : ", end="")
    if advance({(1, 1), (2, 1), (3, 1)}) == {(2, 1), (2, 0), (2, 2)}:
        print("OK")
    else:
        print("FAILED")
        failures.append("Test 4: reproduction")

    print("overpopulation : ", end="")
    if advance({(1, 1), (3, 1), (1, 3), (3, 3), (2, 2)}) == {(1, 2), (2, 1), (2, 3), (3, 2)}:
        print("OK")
    else:
        print("FAILED")
        failures.append("Test 5 : overpopulation")


    return failures


def run_tests():
    print("== testing advance ==")
    failures = test_advance()
    for fail_string in failures:
        print(fail_string)


if __name__ == "__main__":
    run_tests()