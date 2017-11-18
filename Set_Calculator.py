from Operations import *
from Parser import *


while True:
    universe_of_discourse = []
    merged = []
    setA = []
    setB = []

    universe = input('Universe of Discourse: ')
    # Hint: {a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z} - no space, use {}

    equation = input('Equation: ')
    # Hint: {a,b,c} U {d,e,f} = Union
    # Hint: {a,b,c} I {a,b,c,d,e,f} = Intersection
    # Hint: {a,b,c} D {a,b,c,d,e,f} = Difference
    # Hint: {a,b,c} C {d,e,f} = Cartesian Product
    # Hint: {a,b,c} P = Power Set

    merged = equation.split(' ')
    universe_of_discourse = reduce_set(universe)
    print('Universe of Discourse: ' + str(universe_of_discourse))

    if len(merged) == 3:
        operation = merged.pop(1)
        setB = reduce_set(merged)
        setA = reduce_set(merged)

        if check_sets(setA, universe_of_discourse) and check_sets(setB, universe_of_discourse):
            if operation == 'U':
                union(setA, setB)
            elif operation == 'I':
                intersection(setA, setB)
            elif operation == 'D':
                difference(setA, setB)
            elif operation == 'C':
                cartesian_product(setA, setB)
        else:
            print('Invalid Inputs')

    elif len(merged) == 2:
        operation = merged.pop()
        setA = reduce_set(merged)

        if check_sets(setA, universe_of_discourse):
            if operation == 'P':
                power_set(setA)
        else:
            print('Invalid Inputs')

    else:
        print('Invalid Inputs')
