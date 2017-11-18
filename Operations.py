from itertools import *


def union(setA, setB):

    result = setA + setB
    print("Union: " + str(result))


def intersection(setA, setB):

    result = set(setA) & set(setB)
    print("Intersection: " + str(result))


def difference(setA, setB):

    result = set(setA) - set(setB)

    print("Difference: " + str(result))


def cartesian_product(setA, setB):

    result = list(product(setA, setB))

    print("Cartesian Product: " + str(result))


def power_set(iterable):
    # Power Set([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    result = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    print("Power Set: " + str(result))