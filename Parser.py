def check_sets(sets, universe_of_discourse):
    if set(sets).issubset(universe_of_discourse):
        return True
    else:
        return False


def reduce_set(merged):
    if type(merged) is list:
        new_set = merged.pop()
    else:
        new_set = merged

    A = list(new_set)

    if "{" in A:
        A.remove('{')
    if "}" in A:
        A.remove('}')

    while ',' in A:
        A.remove(',')

    return A
