import math
from math import sqrt,ceil,floor,log10
from timeit import Timer
from decimal import *
from fractions import Fraction
from functools import reduce
from operator import mul
import itertools
from itertools import *
import sys
import argparse
import inspect

import logging
l = logging.getLogger(__name__)


def euler001():
    """Solution to project euler problem 1"""
    multiples = []
    for i in range(3,1000):
        #print(i)
        if (i%3 == 0 or i%5 == 0):
            multiples.append(i)
    print(sum(multiples))

def euler1set():
    """arst"""
    s = {i for i in range(3,1000,3)}
    s.update([i for i in range(5,1000,5)])
    print(sum(s))

def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     fibs = []
     a, b = 0, 1
     while a < n:
         if (a%2 == 0):
             fibs.append(a)
         a, b = b, a+b
     return sum(fibs)

def euler2():
    print(fib(4000000))

def euler3():
    """ """
    composite = 600851475143 
    for i in range(2,int(math.sqrt(composite))):
        if (composite % i == 0):
            print(i)

def euler6():
    n = 100
    sumOfSquares = sum([x**2 for x in range(1,n+1)])
    squareOfSums = sum(range(1,n+1))**2
    print(abs( sumOfSquares - squareOfSums))

def euler007():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and
    13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    tenthpower = 6
    while len(primeSieve2(10 ** tenthpower)) < 10000:
        tenthpower += 1
    lps = primeSieve2(10 ** tenthpower)
    lps.sort()
    assert lps[5] == 13
    return lps[10000] # 0 indexed, so 10000 is the 10001st prime.

# let's move the input to files so that we don't have giant strings
# present in the code.

# it's key to note that we never process the number as one number,
# we are only ever concerned with groups of digits,
# so there is no requirement for bignums.
def euler8():
    """
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    """
    with open('euler8.input') as f:
        input = f.read()
    input = input.replace('\n','') # make a single giant string
    assert len(input) == 1000
    # brute force algorithm is to calculate each length 13 subslice and find the biggest one.
    # optimization one is skipping any subset with a 0 in it, as 0 product always results in 0
    # optimization two is to multiply in the next number and divide out the previous number.
    # Still needs zero skipping logic.
    maxprod = 0
    for i in range(0,1000-13):
        subset = input[i:i+13] # calculate every length 13 subset
        assert len(subset) == 13
        # split each slice into indivdual chars, convert to numbers, calculate product of numbers
        prod = reduce(lambda x,y: x*y, [int(d) for d in subset])
        if prod > maxprod: # save the biggest value seen
           maxprod = prod
    return maxprod

def euler9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    # brute force with the constraints a < b < c.
    for a in range(1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                if a ** 2 + b ** 2 == c ** 2:
                    if a + b + c == 1000:
                        return a * b * c

def euler10():
    return sum(primeSieve2(2_000_000))

def euler011():
    x = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66  88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    y = x.split()
    lines = []
    for i in range(0,20):
        line = []
        for j in range(0,20):
        	line.append(int(y[j+(i*20)]))
        print(line)
        lines.append(line)
    z = lines
    
    print()
    max = 0
    count = 0
    '''left to right,
    top to bottom,
    up-left to lower-right,
    up-right to lower-left'''
    print (count)
    LtoRproducts = []
    for i in range(0,20):
        productLine = []
        for j in range(0,16):
            product = 1;
            for k in range(0,4):
                product *= z[i][j+k]
                #print(product)
            if (product > max):
                max = product
            count += 1
            #productLine.append(z[i][j] * z[i][j+1] * z[i][j+2] * z[i][j+3])
            productLine.append(product)
        #print(productLine)
        LtoRproducts.append(productLine)
    print (count)
    TtoBproducts = []
    for i in range(0,16):
        productLine = []
        for j in range(0,20):
            product = 1;
            for k in range(0,4):
                product *= z[i+k][j]
                #print(product)
            if (product > max):
                max = product
            count += 1
            #productLine.append(z[i][j] * z[i][j+1] * z[i][j+2] * z[i][j+3])
            productLine.append(product)
        #print(productLine)
        LtoRproducts.append(productLine)

    print (count)
    LDiagProducts = []
    for i in range(0,17):
        productLine = []
        for j in range(0,17):
            product = 1;
            for k in range(0,4):
                product *= z[i+k][j+k]
                #print(product)
            if (product > max):
                max = product
            count += 1
            productLine.append(product)
        LDiagProducts.append(productLine)

    print (count)
    RDiagProducts = []
    for i in range(0,17): #row
        productLine = []
        for j in range(19,4,-1):
            product = 1;
            for k in range(0,4):
                product *= z[i+k][j-k]
                print( i, j, k, i-k, j-k, z[i-k][j-k])
            if (product > max):
                max = product
            count += 1
            productLine.append(product)
        print(productLine)
        RDiagProducts.append(productLine)
    print (count)
    return max

def triangleNumber(n):
    ''' The n-th triangle number'''
    return (n*(n+1))//2

def pentagonalNumber(n):
    return n*(3*n-1)//2

def hexagonalNumber(n):
    return n*(2*n-1)

def euler045(limit = 300000):
    '''finish 401am jul 22 2011'''
    t= set()
    p = set()
    h = set()
    for i in range(1,limit):
        t.add(triangleNumber(i))
        p.add(pentagonalNumber(i))
        h.add(hexagonalNumber(i))
    x = t.intersection(p,h)
    print (x)
    
def euler012(n = 500):
    i = 1
    while(True):
        if(i%100000==0):
            print(i)
        if(divisorFunction(triangleNumber(i)) >= n):
           return triangleNumber(i)
        i+=1

def euler13():
    """
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    """
    with open('../input/euler13.input') as f:
        input = f.read().splitlines()
    acc = 0
    for n in input:
        acc += int(n) 
    return str(acc)[0:10]

def euler14(max: int = 1_000_000):
    """
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    # brute force, go through each chain, and count the length of the path.
    # second version, first optimization is to put the key, value being, number and path length.
    maxLength = 0
    maxLengthC = 2
    for i in range(2, max):
        length = 0
        nextC = i
        while nextC != 1:
            length +=1
            nextC = nextCollatz(nextC)
        if length > maxLength:
            maxLength = length
            maxLengthC = i
    return maxLengthC

def nextCollatz(n: int):
    if n % 2 == 0: # even
        return n//2
    else:
        return 3*n + 1

collatzTable: dict[int, int] = {1:1, 2:2} #, 4:3, 8:4,16:5, 5:6, 10:7,20:8,40:9,13:10}

def euler14hash(max: int = 1_000_000):
    for i in range(2, max):
        nextCollatzTable(i)
        # print(n, i)
    maxLoc= 0
    max = 0
    for k in collatzTable:
        ksize = collatzTable[k]
        if ksize > max and k < 1_000_000:
            maxLoc = k
            max = ksize
    return maxLoc

def nextCollatzTable(n: int) -> int:
    nextLen = 0
    if n not in collatzTable:
        if n % 2 == 0: # even
            next = n//2
            if next not in collatzTable:
                nextLen = nextCollatzTable(next) + 1
                # print(nextLen)
                collatzTable[next] = nextLen
        else:
            next = 3*n + 1
            if next not in collatzTable:
                nextLen = nextCollatzTable(next) + 1
                # print(nextLen)
                collatzTable[next] = nextLen
        nextLen = collatzTable[next]
        collatzTable[n] = nextLen + 1
    # print(collatzTable)
    # print("return", collatzTable[n])
    return collatzTable[n]

def euler15():
    # this looks more like a paper and pencil one than possibly a calculation one.
    # 1x1 has 2 ways
    # 2x2 has 6 ways, as given
    # 3x3 has
    # 20x20 is 20 rights, and 20 downs. 40 moves total. so it's like 40 chose 20 kind of permutation
    # this is actually called a combinatoric, which makes sense, because we're evaluating combinations of choices.
    assert math.comb(2,1) == 2
    assert math.comb(4,2) == 6
    return math.comb(40,20)

def findMinTriNum():
    i = 0
    while True:
        if triangleNumber(i) >= 2**500:
            return i
        i+=1

factorTable = {1:[],2:[(2,1)]}

triangleTest = '''3
7 4
2 4 6
8 5 9 3'''

eighteenData = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

sixtySevenData = '''59
73 41
52 40 09
26 53 06 34
10 51 87 86 81
61 95 66 57 25 68
90 81 80 38 92 67 73
30 28 51 76 81 18 75 44
84 14 95 87 62 81 17 78 58
21 46 71 58 02 79 62 39 31 09
56 34 35 53 78 31 81 18 90 93 15
78 53 04 21 84 93 32 13 97 11 37 51
45 03 81 79 05 18 78 86 13 30 63 99 95
39 87 96 28 03 38 42 17 82 87 58 07 22 57
06 17 51 17 07 93 09 07 75 97 95 78 87 08 53
67 66 59 60 88 99 94 65 55 77 55 34 27 53 78 28
76 40 41 04 87 16 09 42 75 69 23 97 30 60 10 79 87
12 10 44 26 21 36 32 84 98 60 13 12 36 16 63 31 91 35
70 39 06 05 55 27 38 48 28 22 34 35 62 62 15 14 94 89 86
66 56 68 84 96 21 34 34 34 81 62 40 65 54 62 05 98 03 02 60
38 89 46 37 99 54 34 53 36 14 70 26 02 90 45 13 31 61 83 73 47
36 10 63 96 60 49 41 05 37 42 14 58 84 93 96 17 09 43 05 43 06 59
66 57 87 57 61 28 37 51 84 73 79 15 39 95 88 87 43 39 11 86 77 74 18
54 42 05 79 30 49 99 73 46 37 50 02 45 09 54 52 27 95 27 65 19 45 26 45
71 39 17 78 76 29 52 90 18 99 78 19 35 62 71 19 23 65 93 85 49 33 75 09 02
33 24 47 61 60 55 32 88 57 55 91 54 46 57 07 77 98 52 80 99 24 25 46 78 79 05
92 09 13 55 10 67 26 78 76 82 63 49 51 31 24 68 05 57 07 54 69 21 67 43 17 63 12
24 59 06 08 98 74 66 26 61 60 13 03 09 09 24 30 71 08 88 70 72 70 29 90 11 82 41 34
66 82 67 04 36 60 92 77 91 85 62 49 59 61 30 90 29 94 26 41 89 04 53 22 83 41 09 74 90
48 28 26 37 28 52 77 26 51 32 18 98 79 36 62 13 17 08 19 54 89 29 73 68 42 14 08 16 70 37
37 60 69 70 72 71 09 59 13 60 38 13 57 36 09 30 43 89 30 39 15 02 44 73 05 73 26 63 56 86 12
55 55 85 50 62 99 84 77 28 85 03 21 27 22 19 26 82 69 54 04 13 07 85 14 01 15 70 59 89 95 10 19
04 09 31 92 91 38 92 86 98 75 21 05 64 42 62 84 36 20 73 42 21 23 22 51 51 79 25 45 85 53 03 43 22
75 63 02 49 14 12 89 14 60 78 92 16 44 82 38 30 72 11 46 52 90 27 08 65 78 03 85 41 57 79 39 52 33 48
78 27 56 56 39 13 19 43 86 72 58 95 39 07 04 34 21 98 39 15 39 84 89 69 84 46 37 57 59 35 59 50 26 15 93
42 89 36 27 78 91 24 11 17 41 05 94 07 69 51 96 03 96 47 90 90 45 91 20 50 56 10 32 36 49 04 53 85 92 25 65
52 09 61 30 61 97 66 21 96 92 98 90 06 34 96 60 32 69 68 33 75 84 18 31 71 50 84 63 03 03 19 11 28 42 75 45 45
61 31 61 68 96 34 49 39 05 71 76 59 62 67 06 47 96 99 34 21 32 47 52 07 71 60 42 72 94 56 82 83 84 40 94 87 82 46
01 20 60 14 17 38 26 78 66 81 45 95 18 51 98 81 48 16 53 88 37 52 69 95 72 93 22 34 98 20 54 27 73 61 56 63 60 34 63
93 42 94 83 47 61 27 51 79 79 45 01 44 73 31 70 83 42 88 25 53 51 30 15 65 94 80 44 61 84 12 77 02 62 02 65 94 42 14 94
32 73 09 67 68 29 74 98 10 19 85 48 38 31 85 67 53 93 93 77 47 67 39 72 94 53 18 43 77 40 78 32 29 59 24 06 02 83 50 60 66
32 01 44 30 16 51 15 81 98 15 10 62 86 79 50 62 45 60 70 38 31 85 65 61 64 06 69 84 14 22 56 43 09 48 66 69 83 91 60 40 36 61
92 48 22 99 15 95 64 43 01 16 94 02 99 19 17 69 11 58 97 56 89 31 77 45 67 96 12 73 08 20 36 47 81 44 50 64 68 85 40 81 85 52 09
91 35 92 45 32 84 62 15 19 64 21 66 06 01 52 80 62 59 12 25 88 28 91 50 40 16 22 99 92 79 87 51 21 77 74 77 07 42 38 42 74 83 02 05
46 19 77 66 24 18 05 32 02 84 31 99 92 58 96 72 91 36 62 99 55 29 53 42 12 37 26 58 89 50 66 19 82 75 12 48 24 87 91 85 02 07 03 76 86
99 98 84 93 07 17 33 61 92 20 66 60 24 66 40 30 67 05 37 29 24 96 03 27 70 62 13 04 45 47 59 88 43 20 66 15 46 92 30 04 71 66 78 70 53 99
67 60 38 06 88 04 17 72 10 99 71 07 42 25 54 05 26 64 91 50 45 71 06 30 67 48 69 82 08 56 80 67 18 46 66 63 01 20 08 80 47 07 91 16 03 79 87
18 54 78 49 80 48 77 40 68 23 60 88 58 80 33 57 11 69 55 53 64 02 94 49 60 92 16 35 81 21 82 96 25 24 96 18 02 05 49 03 50 77 06 32 84 27 18 38
68 01 50 04 03 21 42 94 53 24 89 05 92 26 52 36 68 11 85 01 04 42 02 45 15 06 50 04 53 73 25 74 81 88 98 21 67 84 79 97 99 20 95 04 40 46 02 58 87
94 10 02 78 88 52 21 03 88 60 06 53 49 71 20 91 12 65 07 49 21 22 11 41 58 99 36 16 09 48 17 24 52 36 23 15 72 16 84 56 02 99 43 76 81 71 29 39 49 17
64 39 59 84 86 16 17 66 03 09 43 06 64 18 63 29 68 06 23 07 87 14 26 35 17 12 98 41 53 64 78 18 98 27 28 84 80 67 75 62 10 11 76 90 54 10 05 54 41 39 66
43 83 18 37 32 31 52 29 95 47 08 76 35 11 04 53 35 43 34 10 52 57 12 36 20 39 40 55 78 44 07 31 38 26 08 15 56 88 86 01 52 62 10 24 32 05 60 65 53 28 57 99
03 50 03 52 07 73 49 92 66 80 01 46 08 67 25 36 73 93 07 42 25 53 13 96 76 83 87 90 54 89 78 22 78 91 73 51 69 09 79 94 83 53 09 40 69 62 10 79 49 47 03 81 30
71 54 73 33 51 76 59 54 79 37 56 45 84 17 62 21 98 69 41 95 65 24 39 37 62 03 24 48 54 64 46 82 71 78 33 67 09 16 96 68 52 74 79 68 32 21 13 78 96 60 09 69 20 36
73 26 21 44 46 38 17 83 65 98 07 23 52 46 61 97 33 13 60 31 70 15 36 77 31 58 56 93 75 68 21 36 69 53 90 75 25 82 39 50 65 94 29 30 11 33 11 13 96 02 56 47 07 49 02
76 46 73 30 10 20 60 70 14 56 34 26 37 39 48 24 55 76 84 91 39 86 95 61 50 14 53 93 64 67 37 31 10 84 42 70 48 20 10 72 60 61 84 79 69 65 99 73 89 25 85 48 92 56 97 16
03 14 80 27 22 30 44 27 67 75 79 32 51 54 81 29 65 14 19 04 13 82 04 91 43 40 12 52 29 99 07 76 60 25 01 07 61 71 37 92 40 47 99 66 57 01 43 44 22 40 53 53 09 69 26 81 07
49 80 56 90 93 87 47 13 75 28 87 23 72 79 32 18 27 20 28 10 37 59 21 18 70 04 79 96 03 31 45 71 81 06 14 18 17 05 31 50 92 79 23 47 09 39 47 91 43 54 69 47 42 95 62 46 32 85
37 18 62 85 87 28 64 05 77 51 47 26 30 65 05 70 65 75 59 80 42 52 25 20 44 10 92 17 71 95 52 14 77 13 24 55 11 65 26 91 01 30 63 15 49 48 41 17 67 47 03 68 20 90 98 32 04 40 68
90 51 58 60 06 55 23 68 05 19 76 94 82 36 96 43 38 90 87 28 33 83 05 17 70 83 96 93 06 04 78 47 80 06 23 84 75 23 87 72 99 14 50 98 92 38 90 64 61 58 76 94 36 66 87 80 51 35 61 38
57 95 64 06 53 36 82 51 40 33 47 14 07 98 78 65 39 58 53 06 50 53 04 69 40 68 36 69 75 78 75 60 03 32 39 24 74 47 26 90 13 40 44 71 90 76 51 24 36 50 25 45 70 80 61 80 61 43 90 64 11
18 29 86 56 68 42 79 10 42 44 30 12 96 18 23 18 52 59 02 99 67 46 60 86 43 38 55 17 44 93 42 21 55 14 47 34 55 16 49 24 23 29 96 51 55 10 46 53 27 92 27 46 63 57 30 65 43 27 21 20 24 83
81 72 93 19 69 52 48 01 13 83 92 69 20 48 69 59 20 62 05 42 28 89 90 99 32 72 84 17 08 87 36 03 60 31 36 36 81 26 97 36 48 54 56 56 27 16 91 08 23 11 87 99 33 47 02 14 44 73 70 99 43 35 33
90 56 61 86 56 12 70 59 63 32 01 15 81 47 71 76 95 32 65 80 54 70 34 51 40 45 33 04 64 55 78 68 88 47 31 47 68 87 03 84 23 44 89 72 35 08 31 76 63 26 90 85 96 67 65 91 19 14 17 86 04 71 32 95
37 13 04 22 64 37 37 28 56 62 86 33 07 37 10 44 52 82 52 06 19 52 57 75 90 26 91 24 06 21 14 67 76 30 46 14 35 89 89 41 03 64 56 97 87 63 22 34 03 79 17 45 11 53 25 56 96 61 23 18 63 31 37 37 47
77 23 26 70 72 76 77 04 28 64 71 69 14 85 96 54 95 48 06 62 99 83 86 77 97 75 71 66 30 19 57 90 33 01 60 61 14 12 90 99 32 77 56 41 18 14 87 49 10 14 90 64 18 50 21 74 14 16 88 05 45 73 82 47 74 44
22 97 41 13 34 31 54 61 56 94 03 24 59 27 98 77 04 09 37 40 12 26 87 09 71 70 07 18 64 57 80 21 12 71 83 94 60 39 73 79 73 19 97 32 64 29 41 07 48 84 85 67 12 74 95 20 24 52 41 67 56 61 29 93 35 72 69
72 23 63 66 01 11 07 30 52 56 95 16 65 26 83 90 50 74 60 18 16 48 43 77 37 11 99 98 30 94 91 26 62 73 45 12 87 73 47 27 01 88 66 99 21 41 95 80 02 53 23 32 61 48 32 43 43 83 14 66 95 91 19 81 80 67 25 88
08 62 32 18 92 14 83 71 37 96 11 83 39 99 05 16 23 27 10 67 02 25 44 11 55 31 46 64 41 56 44 74 26 81 51 31 45 85 87 09 81 95 22 28 76 69 46 48 64 87 67 76 27 89 31 11 74 16 62 03 60 94 42 47 09 34 94 93 72
56 18 90 18 42 17 42 32 14 86 06 53 33 95 99 35 29 15 44 20 49 59 25 54 34 59 84 21 23 54 35 90 78 16 93 13 37 88 54 19 86 67 68 55 66 84 65 42 98 37 87 56 33 28 58 38 28 38 66 27 52 21 81 15 08 22 97 32 85 27
91 53 40 28 13 34 91 25 01 63 50 37 22 49 71 58 32 28 30 18 68 94 23 83 63 62 94 76 80 41 90 22 82 52 29 12 18 56 10 08 35 14 37 57 23 65 67 40 72 39 93 39 70 89 40 34 07 46 94 22 20 05 53 64 56 30 05 56 61 88 27
23 95 11 12 37 69 68 24 66 10 87 70 43 50 75 07 62 41 83 58 95 93 89 79 45 39 02 22 05 22 95 43 62 11 68 29 17 40 26 44 25 71 87 16 70 85 19 25 59 94 90 41 41 80 61 70 55 60 84 33 95 76 42 63 15 09 03 40 38 12 03 32
09 84 56 80 61 55 85 97 16 94 82 94 98 57 84 30 84 48 93 90 71 05 95 90 73 17 30 98 40 64 65 89 07 79 09 19 56 36 42 30 23 69 73 72 07 05 27 61 24 31 43 48 71 84 21 28 26 65 65 59 65 74 77 20 10 81 61 84 95 08 52 23 70
47 81 28 09 98 51 67 64 35 51 59 36 92 82 77 65 80 24 72 53 22 07 27 10 21 28 30 22 48 82 80 48 56 20 14 43 18 25 50 95 90 31 77 08 09 48 44 80 90 22 93 45 82 17 13 96 25 26 08 73 34 99 06 49 24 06 83 51 40 14 15 10 25 01
54 25 10 81 30 64 24 74 75 80 36 75 82 60 22 69 72 91 45 67 03 62 79 54 89 74 44 83 64 96 66 73 44 30 74 50 37 05 09 97 70 01 60 46 37 91 39 75 75 18 58 52 72 78 51 81 86 52 08 97 01 46 43 66 98 62 81 18 70 93 73 08 32 46 34
96 80 82 07 59 71 92 53 19 20 88 66 03 26 26 10 24 27 50 82 94 73 63 08 51 33 22 45 19 13 58 33 90 15 22 50 36 13 55 06 35 47 82 52 33 61 36 27 28 46 98 14 73 20 73 32 16 26 80 53 47 66 76 38 94 45 02 01 22 52 47 96 64 58 52 39
88 46 23 39 74 63 81 64 20 90 33 33 76 55 58 26 10 46 42 26 74 74 12 83 32 43 09 02 73 55 86 54 85 34 28 23 29 79 91 62 47 41 82 87 99 22 48 90 20 05 96 75 95 04 43 28 81 39 81 01 28 42 78 25 39 77 90 57 58 98 17 36 73 22 63 74 51
29 39 74 94 95 78 64 24 38 86 63 87 93 06 70 92 22 16 80 64 29 52 20 27 23 50 14 13 87 15 72 96 81 22 08 49 72 30 70 24 79 31 16 64 59 21 89 34 96 91 48 76 43 53 88 01 57 80 23 81 90 79 58 01 80 87 17 99 86 90 72 63 32 69 14 28 88 69
37 17 71 95 56 93 71 35 43 45 04 98 92 94 84 96 11 30 31 27 31 60 92 03 48 05 98 91 86 94 35 90 90 08 48 19 33 28 68 37 59 26 65 96 50 68 22 07 09 49 34 31 77 49 43 06 75 17 81 87 61 79 52 26 27 72 29 50 07 98 86 01 17 10 46 64 24 18 56
51 30 25 94 88 85 79 91 40 33 63 84 49 67 98 92 15 26 75 19 82 05 18 78 65 93 61 48 91 43 59 41 70 51 22 15 92 81 67 91 46 98 11 11 65 31 66 10 98 65 83 21 05 56 05 98 73 67 46 74 69 34 08 30 05 52 07 98 32 95 30 94 65 50 24 63 28 81 99 57
19 23 61 36 09 89 71 98 65 17 30 29 89 26 79 74 94 11 44 48 97 54 81 55 39 66 69 45 28 47 13 86 15 76 74 70 84 32 36 33 79 20 78 14 41 47 89 28 81 05 99 66 81 86 38 26 06 25 13 60 54 55 23 53 27 05 89 25 23 11 13 54 59 54 56 34 16 24 53 44 06
13 40 57 72 21 15 60 08 04 19 11 98 34 45 09 97 86 71 03 15 56 19 15 44 97 31 90 04 87 87 76 08 12 30 24 62 84 28 12 85 82 53 99 52 13 94 06 65 97 86 09 50 94 68 69 74 30 67 87 94 63 07 78 27 80 36 69 41 06 92 32 78 37 82 30 05 18 87 99 72 19 99
44 20 55 77 69 91 27 31 28 81 80 27 02 07 97 23 95 98 12 25 75 29 47 71 07 47 78 39 41 59 27 76 13 15 66 61 68 35 69 86 16 53 67 63 99 85 41 56 08 28 33 40 94 76 90 85 31 70 24 65 84 65 99 82 19 25 54 37 21 46 33 02 52 99 51 33 26 04 87 02 08 18 96
54 42 61 45 91 06 64 79 80 82 32 16 83 63 42 49 19 78 65 97 40 42 14 61 49 34 04 18 25 98 59 30 82 72 26 88 54 36 21 75 03 88 99 53 46 51 55 78 22 94 34 40 68 87 84 25 30 76 25 08 92 84 42 61 40 38 09 99 40 23 29 39 46 55 10 90 35 84 56 70 63 23 91 39
52 92 03 71 89 07 09 37 68 66 58 20 44 92 51 56 13 71 79 99 26 37 02 06 16 67 36 52 58 16 79 73 56 60 59 27 44 77 94 82 20 50 98 33 09 87 94 37 40 83 64 83 58 85 17 76 53 02 83 52 22 27 39 20 48 92 45 21 09 42 24 23 12 37 52 28 50 78 79 20 86 62 73 20 59
54 96 80 15 91 90 99 70 10 09 58 90 93 50 81 99 54 38 36 10 30 11 35 84 16 45 82 18 11 97 36 43 96 79 97 65 40 48 23 19 17 31 64 52 65 65 37 32 65 76 99 79 34 65 79 27 55 33 03 01 33 27 61 28 66 08 04 70 49 46 48 83 01 45 19 96 13 81 14 21 31 79 93 85 50 05
92 92 48 84 59 98 31 53 23 27 15 22 79 95 24 76 05 79 16 93 97 89 38 89 42 83 02 88 94 95 82 21 01 97 48 39 31 78 09 65 50 56 97 61 01 07 65 27 21 23 14 15 80 97 44 78 49 35 33 45 81 74 34 05 31 57 09 38 94 07 69 54 69 32 65 68 46 68 78 90 24 28 49 51 45 86 35
41 63 89 76 87 31 86 09 46 14 87 82 22 29 47 16 13 10 70 72 82 95 48 64 58 43 13 75 42 69 21 12 67 13 64 85 58 23 98 09 37 76 05 22 31 12 66 50 29 99 86 72 45 25 10 28 19 06 90 43 29 31 67 79 46 25 74 14 97 35 76 37 65 46 23 82 06 22 30 76 93 66 94 17 96 13 20 72
63 40 78 08 52 09 90 41 70 28 36 14 46 44 85 96 24 52 58 15 87 37 05 98 99 39 13 61 76 38 44 99 83 74 90 22 53 80 56 98 30 51 63 39 44 30 91 91 04 22 27 73 17 35 53 18 35 45 54 56 27 78 48 13 69 36 44 38 71 25 30 56 15 22 73 43 32 69 59 25 93 83 45 11 34 94 44 39 92
12 36 56 88 13 96 16 12 55 54 11 47 19 78 17 17 68 81 77 51 42 55 99 85 66 27 81 79 93 42 65 61 69 74 14 01 18 56 12 01 58 37 91 22 42 66 83 25 19 04 96 41 25 45 18 69 96 88 36 93 10 12 98 32 44 83 83 04 72 91 04 27 73 07 34 37 71 60 59 31 01 54 54 44 96 93 83 36 04 45
30 18 22 20 42 96 65 79 17 41 55 69 94 81 29 80 91 31 85 25 47 26 43 49 02 99 34 67 99 76 16 14 15 93 08 32 99 44 61 77 67 50 43 55 87 55 53 72 17 46 62 25 50 99 73 05 93 48 17 31 70 80 59 09 44 59 45 13 74 66 58 94 87 73 16 14 85 38 74 99 64 23 79 28 71 42 20 37 82 31 23
51 96 39 65 46 71 56 13 29 68 53 86 45 33 51 49 12 91 21 21 76 85 02 17 98 15 46 12 60 21 88 30 92 83 44 59 42 50 27 88 46 86 94 73 45 54 23 24 14 10 94 21 20 34 23 51 04 83 99 75 90 63 60 16 22 33 83 70 11 32 10 50 29 30 83 46 11 05 31 17 86 42 49 01 44 63 28 60 07 78 95 40
44 61 89 59 04 49 51 27 69 71 46 76 44 04 09 34 56 39 15 06 94 91 75 90 65 27 56 23 74 06 23 33 36 69 14 39 05 34 35 57 33 22 76 46 56 10 61 65 98 09 16 69 04 62 65 18 99 76 49 18 72 66 73 83 82 40 76 31 89 91 27 88 17 35 41 35 32 51 32 67 52 68 74 85 80 57 07 11 62 66 47 22 67
65 37 19 97 26 17 16 24 24 17 50 37 64 82 24 36 32 11 68 34 69 31 32 89 79 93 96 68 49 90 14 23 04 04 67 99 81 74 70 74 36 96 68 09 64 39 88 35 54 89 96 58 66 27 88 97 32 14 06 35 78 20 71 06 85 66 57 02 58 91 72 05 29 56 73 48 86 52 09 93 22 57 79 42 12 01 31 68 17 59 63 76 07 77
73 81 14 13 17 20 11 09 01 83 08 85 91 70 84 63 62 77 37 07 47 01 59 95 39 69 39 21 99 09 87 02 97 16 92 36 74 71 90 66 33 73 73 75 52 91 11 12 26 53 05 26 26 48 61 50 90 65 01 87 42 47 74 35 22 73 24 26 56 70 52 05 48 41 31 18 83 27 21 39 80 85 26 08 44 02 71 07 63 22 05 52 19 08 20
17 25 21 11 72 93 33 49 64 23 53 82 03 13 91 65 85 02 40 05 42 31 77 42 05 36 06 54 04 58 07 76 87 83 25 57 66 12 74 33 85 37 74 32 20 69 03 97 91 68 82 44 19 14 89 28 85 85 80 53 34 87 58 98 88 78 48 65 98 40 11 57 10 67 70 81 60 79 74 72 97 59 79 47 30 20 54 80 89 91 14 05 33 36 79 39
60 85 59 39 60 07 57 76 77 92 06 35 15 72 23 41 45 52 95 18 64 79 86 53 56 31 69 11 91 31 84 50 44 82 22 81 41 40 30 42 30 91 48 94 74 76 64 58 74 25 96 57 14 19 03 99 28 83 15 75 99 01 89 85 79 50 03 95 32 67 44 08 07 41 62 64 29 20 14 76 26 55 48 71 69 66 19 72 44 25 14 01 48 74 12 98 07
64 66 84 24 18 16 27 48 20 14 47 69 30 86 48 40 23 16 61 21 51 50 26 47 35 33 91 28 78 64 43 68 04 79 51 08 19 60 52 95 06 68 46 86 35 97 27 58 04 65 30 58 99 12 12 75 91 39 50 31 42 64 70 04 46 07 98 73 98 93 37 89 77 91 64 71 64 65 66 21 78 62 81 74 42 20 83 70 73 95 78 45 92 27 34 53 71 15
30 11 85 31 34 71 13 48 05 14 44 03 19 67 23 73 19 57 06 90 94 72 57 69 81 62 59 68 88 57 55 69 49 13 07 87 97 80 89 05 71 05 05 26 38 40 16 62 45 99 18 38 98 24 21 26 62 74 69 04 85 57 77 35 58 67 91 79 79 57 86 28 66 34 72 51 76 78 36 95 63 90 08 78 47 63 45 31 22 70 52 48 79 94 15 77 61 67 68
23 33 44 81 80 92 93 75 94 88 23 61 39 76 22 03 28 94 32 06 49 65 41 34 18 23 08 47 62 60 03 63 33 13 80 52 31 54 73 43 70 26 16 69 57 87 83 31 03 93 70 81 47 95 77 44 29 68 39 51 56 59 63 07 25 70 07 77 43 53 64 03 94 42 95 39 18 01 66 21 16 97 20 50 90 16 70 10 95 69 29 06 25 61 41 26 15 59 63 35'''

def euler018(triangleText = eighteenData):
    triangle = [[int(i) for i in l.split()] for l in triangleText.splitlines()]
    output = []
    for l,row in enumerate(triangle):
        #print(l+1, row)
        outputRow = []
        for i,num in enumerate(row):
            #print(i,num)
            if(l == 0): # initial
                outputRow.append(num)
            else:
                prevOutRow = output[l-1]
                #print ("previous output Row is",prevOutRow)
                if(i == 0 or i+1 == len(row)): # first or last in a row
                    outNum = 0
                    if i == 0:
                        outNum = num + prevOutRow[0]
                    else:
                        outNum = num + prevOutRow[-1]
                    outputRow.append(outNum)
                    #print(num)
                else:
                    outputRow.append(max([prevOutRow[i] + num, prevOutRow[i-1] + num]))
                    #print(num)
        #print('new row is', outputRow)
        output.append(outputRow)
        #print('out now',output)
    #print(output)
    return (max([max(row) for row in output]))

def euler067():
    return euler018(sixtySevenData)

class bstNode:
    '''
    Node with, left, right, data, key
    '''
    left = None
    right = None
    data = 0
    key = 0


factorTable = {} #{2:[(2,1)],3:[(3,1)]}
divisorTable = {1:[1]}
pdSumTable = {}


def printFactorTable():
    global factorTable
    print(factorTable)

ft = {}        
def newfactor(n):
    orig = n
    global ft
    if n not in ft:
        i = 2;
        f = []
        while i**2 <= n:
            while n%i == 0:
                f.append(i)
                n//=i
            i+=1
        if n > 1: f.append(n)
        ft[orig] = [(x,f.count(x)) for x in set(f)] 
    return ft[orig]

def primeFactors(n):
    return newfactor(n)

def testfactor():
    print(factor(999999000001))
    #print(factor(4398042316799))
    ft = {}
    
#orig

factorTable = {2:[(2,1)],3:[(3,1)]}

def primeFactor(number):
   global factorTable
   factors = []
   originalNum = number
   counter = 2
   while counter <= number:
       if number%counter == 0:
           while number%counter == 0:
               numebr = number/counter
               hashFactors(number)
               factors.append(counter)
       else:
           counter = counter + 1
   return [(x,factors.count(x)) for x in set(factors)]

def printFactorTable():
   global factorTable
   print (factorTable)

def hashFactors(number):
   global factorTable
   if number not in factorTable:
       factorTable[number] = primeFactor(number)
       return factorTable[number]
   else:
       return factorTable[number]

#orig end

#
def testNewFactors(end = 10000):
    for i in range(1,end):
        newfactor(i)

def testOldFactors(end=10000):
    for i in range(1,end):
        #print (i, hashFactors(3)) 
        hashFactors(i)

def testEquivalence():
    for i in range(1,10000):
        assert newfactor(i) == hashFactors(i)

def test():
    t = Timer("testNewFactors()", "from __main__ import testNewFactors")
    print(t.timeit(1))
    print(t.timeit(1))
    t = Timer("testOldFactors()", "from __main__ import testOldFactors")
    print(t.timeit(1))
    print(t.timeit(1))
    t = Timer("testEquivalence()", "from __main__ import testEquivalence")
    print(t.timeit(1))
    print(t.timeit(1))
   
def properDivisors(n):
    global divisorTable
    if n in divisorTable:
        return divisorTable[n]
    else:
        l = [item for sublist in [list(repeat(x,y)) for (x,y) in primeFactors(n)] for item in sublist]
        s = set()
        for i in range(len(l)):
            for x in itertools.combinations(l, i):
                #print(x)
                s.add(x)
        if () in s: s.remove(())
        divs = ([reduce(mul,x) for x in s] + [1])
        divisorTable[n] = divs
        return divs

def perfectNumber(n):
    '''returns true if n is perfect'''
    return sum(properDivisors(n)) == n

def deficientNumber(n):
    '''returns true if n is deficient'''
    return sum(properDivisors(n)) < n

def abundantNumber(n):
    '''returns true if n is abundant'''
    return sum(properDivisors(n)) > n

def divisorFunction(n):
    return len(properDivisors(n))

def pdSum(n):
    global pdSumTable
    if n not in pdSumTable:
        l = properDivisors(n)
        pdSumTable[n] = (sum(l))
    return pdSumTable[n]

def euler021(upperlimit = 9999):
    s = set()
    for a in range(2,upperlimit):
        b = pdSum(a)
        if (a != b and b < 10000 and a == pdSum(b) and b == pdSum(a)):
            s.update([a,b])
    print(s)
    return sum(s)

#assert euler021() == 31626

def euler019(n = 1001):
    accum = 1
    i = 1
    for spiral in range(3,n+1,2):
        s = spiral//2
        for j in range(4):
            i += (s*2)
            accum += i
            #print(i,accum)
    return accum

euler017Data = '''onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteentwentytwenty-onetwenty-twotwenty-threetwenty-fourtwenty-fivetwenty-sixtwenty-seventwenty-eighttwenty-ninethirtythirty-onethirty-twothirty-threethirty-fourthirty-fivethirty-sixthirty-seventhirty-eightthirty-ninefortyforty-oneforty-twoforty-threeforty-fourforty-fiveforty-sixforty-sevenforty-eightforty-ninefiftyfifty-onefifty-twofifty-threefifty-fourfifty-fivefifty-sixfifty-sevenfifty-eightfifty-ninesixtysixty-onesixty-twosixty-threesixty-foursixty-fivesixty-sixsixty-sevensixty-eightsixty-nineseventyseventy-oneseventy-twoseventy-threeseventy-fourseventy-fiveseventy-sixseventy-sevenseventy-eightseventy-nineeightyeighty-oneeighty-twoeighty-threeeighty-foureighty-fiveeighty-sixeighty-seveneighty-eighteighty-nineninetyninety-oneninety-twoninety-threeninety-fourninety-fiveninety-sixninety-sevenninety-eightninety-nineone hundredone hundred and oneone hundred and twoone hundred and threeone hundred and fourone hundred and fiveone hundred and sixone hundred and sevenone hundred and eightone hundred and nineone hundred and tenone hundred and elevenone hundred and twelveone hundred and thirteenone hundred and fourteenone hundred and fifteenone hundred and sixteenone hundred and seventeenone hundred and eighteenone hundred and nineteenone hundred and twentyone hundred and twenty-oneone hundred and twenty-twoone hundred and twenty-threeone hundred and twenty-fourone hundred and twenty-fiveone hundred and twenty-sixone hundred and twenty-sevenone hundred and twenty-eightone hundred and twenty-nineone hundred and thirtyone hundred and thirty-oneone hundred and thirty-twoone hundred and thirty-threeone hundred and thirty-fourone hundred and thirty-fiveone hundred and thirty-sixone hundred and thirty-sevenone hundred and thirty-eightone hundred and thirty-nineone hundred and fortyone hundred and forty-oneone hundred and forty-twoone hundred and forty-threeone hundred and forty-fourone hundred and forty-fiveone hundred and forty-sixone hundred and forty-sevenone hundred and forty-eightone hundred and forty-nineone hundred and fiftyone hundred and fifty-oneone hundred and fifty-twoone hundred and fifty-threeone hundred and fifty-fourone hundred and fifty-fiveone hundred and fifty-sixone hundred and fifty-sevenone hundred and fifty-eightone hundred and fifty-nineone hundred and sixtyone hundred and sixty-oneone hundred and sixty-twoone hundred and sixty-threeone hundred and sixty-fourone hundred and sixty-fiveone hundred and sixty-sixone hundred and sixty-sevenone hundred and sixty-eightone hundred and sixty-nineone hundred and seventyone hundred and seventy-oneone hundred and seventy-twoone hundred and seventy-threeone hundred and seventy-fourone hundred and seventy-fiveone hundred and seventy-sixone hundred and seventy-sevenone hundred and seventy-eightone hundred and seventy-nineone hundred and eightyone hundred and eighty-oneone hundred and eighty-twoone hundred and eighty-threeone hundred and eighty-fourone hundred and eighty-fiveone hundred and eighty-sixone hundred and eighty-sevenone hundred and eighty-eightone hundred and eighty-nineone hundred and ninetyone hundred and ninety-oneone hundred and ninety-twoone hundred and ninety-threeone hundred and ninety-fourone hundred and ninety-fiveone hundred and ninety-sixone hundred and ninety-sevenone hundred and ninety-eightone hundred and ninety-ninetwo hundredtwo hundred and onetwo hundred and twotwo hundred and threetwo hundred and fourtwo hundred and fivetwo hundred and sixtwo hundred and seventwo hundred and eighttwo hundred and ninetwo hundred and tentwo hundred and eleventwo hundred and twelvetwo hundred and thirteentwo hundred and fourteentwo hundred and fifteentwo hundred and sixteentwo hundred and seventeentwo hundred and eighteentwo hundred and nineteentwo hundred and twentytwo hundred and twenty-onetwo hundred and twenty-twotwo hundred and twenty-threetwo hundred and twenty-fourtwo hundred and twenty-fivetwo hundred and twenty-sixtwo hundred and twenty-seventwo hundred and twenty-eighttwo hundred and twenty-ninetwo hundred and thirtytwo hundred and thirty-onetwo hundred and thirty-twotwo hundred and thirty-threetwo hundred and thirty-fourtwo hundred and thirty-fivetwo hundred and thirty-sixtwo hundred and thirty-seventwo hundred and thirty-eighttwo hundred and thirty-ninetwo hundred and fortytwo hundred and forty-onetwo hundred and forty-twotwo hundred and forty-threetwo hundred and forty-fourtwo hundred and forty-fivetwo hundred and forty-sixtwo hundred and forty-seventwo hundred and forty-eighttwo hundred and forty-ninetwo hundred and fiftytwo hundred and fifty-onetwo hundred and fifty-twotwo hundred and fifty-threetwo hundred and fifty-fourtwo hundred and fifty-fivetwo hundred and fifty-sixtwo hundred and fifty-seventwo hundred and fifty-eighttwo hundred and fifty-ninetwo hundred and sixtytwo hundred and sixty-onetwo hundred and sixty-twotwo hundred and sixty-threetwo hundred and sixty-fourtwo hundred and sixty-fivetwo hundred and sixty-sixtwo hundred and sixty-seventwo hundred and sixty-eighttwo hundred and sixty-ninetwo hundred and seventytwo hundred and seventy-onetwo hundred and seventy-twotwo hundred and seventy-threetwo hundred and seventy-fourtwo hundred and seventy-fivetwo hundred and seventy-sixtwo hundred and seventy-seventwo hundred and seventy-eighttwo hundred and seventy-ninetwo hundred and eightytwo hundred and eighty-onetwo hundred and eighty-twotwo hundred and eighty-threetwo hundred and eighty-fourtwo hundred and eighty-fivetwo hundred and eighty-sixtwo hundred and eighty-seventwo hundred and eighty-eighttwo hundred and eighty-ninetwo hundred and ninetytwo hundred and ninety-onetwo hundred and ninety-twotwo hundred and ninety-threetwo hundred and ninety-fourtwo hundred and ninety-fivetwo hundred and ninety-sixtwo hundred and ninety-seventwo hundred and ninety-eighttwo hundred and ninety-ninethree hundredthree hundred and onethree hundred and twothree hundred and threethree hundred and fourthree hundred and fivethree hundred and sixthree hundred and seventhree hundred and eightthree hundred and ninethree hundred and tenthree hundred and eleventhree hundred and twelvethree hundred and thirteenthree hundred and fourteenthree hundred and fifteenthree hundred and sixteenthree hundred and seventeenthree hundred and eighteenthree hundred and nineteenthree hundred and twentythree hundred and twenty-onethree hundred and twenty-twothree hundred and twenty-threethree hundred and twenty-fourthree hundred and twenty-fivethree hundred and twenty-sixthree hundred and twenty-seventhree hundred and twenty-eightthree hundred and twenty-ninethree hundred and thirtythree hundred and thirty-onethree hundred and thirty-twothree hundred and thirty-threethree hundred and thirty-fourthree hundred and thirty-fivethree hundred and thirty-sixthree hundred and thirty-seventhree hundred and thirty-eightthree hundred and thirty-ninethree hundred and fortythree hundred and forty-onethree hundred and forty-twothree hundred and forty-threethree hundred and forty-fourthree hundred and forty-fivethree hundred and forty-sixthree hundred and forty-seventhree hundred and forty-eightthree hundred and forty-ninethree hundred and fiftythree hundred and fifty-onethree hundred and fifty-twothree hundred and fifty-threethree hundred and fifty-fourthree hundred and fifty-fivethree hundred and fifty-sixthree hundred and fifty-seventhree hundred and fifty-eightthree hundred and fifty-ninethree hundred and sixtythree hundred and sixty-onethree hundred and sixty-twothree hundred and sixty-threethree hundred and sixty-fourthree hundred and sixty-fivethree hundred and sixty-sixthree hundred and sixty-seventhree hundred and sixty-eightthree hundred and sixty-ninethree hundred and seventythree hundred and seventy-onethree hundred and seventy-twothree hundred and seventy-threethree hundred and seventy-fourthree hundred and seventy-fivethree hundred and seventy-sixthree hundred and seventy-seventhree hundred and seventy-eightthree hundred and seventy-ninethree hundred and eightythree hundred and eighty-onethree hundred and eighty-twothree hundred and eighty-threethree hundred and eighty-fourthree hundred and eighty-fivethree hundred and eighty-sixthree hundred and eighty-seventhree hundred and eighty-eightthree hundred and eighty-ninethree hundred and ninetythree hundred and ninety-onethree hundred and ninety-twothree hundred and ninety-threethree hundred and ninety-fourthree hundred and ninety-fivethree hundred and ninety-sixthree hundred and ninety-seventhree hundred and ninety-eightthree hundred and ninety-ninefour hundredfour hundred and onefour hundred and twofour hundred and threefour hundred and fourfour hundred and fivefour hundred and sixfour hundred and sevenfour hundred and eightfour hundred and ninefour hundred and tenfour hundred and elevenfour hundred and twelvefour hundred and thirteenfour hundred and fourteenfour hundred and fifteenfour hundred and sixteenfour hundred and seventeenfour hundred and eighteenfour hundred and nineteenfour hundred and twentyfour hundred and twenty-onefour hundred and twenty-twofour hundred and twenty-threefour hundred and twenty-fourfour hundred and twenty-fivefour hundred and twenty-sixfour hundred and twenty-sevenfour hundred and twenty-eightfour hundred and twenty-ninefour hundred and thirtyfour hundred and thirty-onefour hundred and thirty-twofour hundred and thirty-threefour hundred and thirty-fourfour hundred and thirty-fivefour hundred and thirty-sixfour hundred and thirty-sevenfour hundred and thirty-eightfour hundred and thirty-ninefour hundred and fortyfour hundred and forty-onefour hundred and forty-twofour hundred and forty-threefour hundred and forty-fourfour hundred and forty-fivefour hundred and forty-sixfour hundred and forty-sevenfour hundred and forty-eightfour hundred and forty-ninefour hundred and fiftyfour hundred and fifty-onefour hundred and fifty-twofour hundred and fifty-threefour hundred and fifty-fourfour hundred and fifty-fivefour hundred and fifty-sixfour hundred and fifty-sevenfour hundred and fifty-eightfour hundred and fifty-ninefour hundred and sixtyfour hundred and sixty-onefour hundred and sixty-twofour hundred and sixty-threefour hundred and sixty-fourfour hundred and sixty-fivefour hundred and sixty-sixfour hundred and sixty-sevenfour hundred and sixty-eightfour hundred and sixty-ninefour hundred and seventyfour hundred and seventy-onefour hundred and seventy-twofour hundred and seventy-threefour hundred and seventy-fourfour hundred and seventy-fivefour hundred and seventy-sixfour hundred and seventy-sevenfour hundred and seventy-eightfour hundred and seventy-ninefour hundred and eightyfour hundred and eighty-onefour hundred and eighty-twofour hundred and eighty-threefour hundred and eighty-fourfour hundred and eighty-fivefour hundred and eighty-sixfour hundred and eighty-sevenfour hundred and eighty-eightfour hundred and eighty-ninefour hundred and ninetyfour hundred and ninety-onefour hundred and ninety-twofour hundred and ninety-threefour hundred and ninety-fourfour hundred and ninety-fivefour hundred and ninety-sixfour hundred and ninety-sevenfour hundred and ninety-eightfour hundred and ninety-ninefive hundredfive hundred and onefive hundred and twofive hundred and threefive hundred and fourfive hundred and fivefive hundred and sixfive hundred and sevenfive hundred and eightfive hundred and ninefive hundred and tenfive hundred and elevenfive hundred and twelvefive hundred and thirteenfive hundred and fourteenfive hundred and fifteenfive hundred and sixteenfive hundred and seventeenfive hundred and eighteenfive hundred and nineteenfive hundred and twentyfive hundred and twenty-onefive hundred and twenty-twofive hundred and twenty-threefive hundred and twenty-fourfive hundred and twenty-fivefive hundred and twenty-sixfive hundred and twenty-sevenfive hundred and twenty-eightfive hundred and twenty-ninefive hundred and thirtyfive hundred and thirty-onefive hundred and thirty-twofive hundred and thirty-threefive hundred and thirty-fourfive hundred and thirty-fivefive hundred and thirty-sixfive hundred and thirty-sevenfive hundred and thirty-eightfive hundred and thirty-ninefive hundred and fortyfive hundred and forty-onefive hundred and forty-twofive hundred and forty-threefive hundred and forty-fourfive hundred and forty-fivefive hundred and forty-sixfive hundred and forty-sevenfive hundred and forty-eightfive hundred and forty-ninefive hundred and fiftyfive hundred and fifty-onefive hundred and fifty-twofive hundred and fifty-threefive hundred and fifty-fourfive hundred and fifty-fivefive hundred and fifty-sixfive hundred and fifty-sevenfive hundred and fifty-eightfive hundred and fifty-ninefive hundred and sixtyfive hundred and sixty-onefive hundred and sixty-twofive hundred and sixty-threefive hundred and sixty-fourfive hundred and sixty-fivefive hundred and sixty-sixfive hundred and sixty-sevenfive hundred and sixty-eightfive hundred and sixty-ninefive hundred and seventyfive hundred and seventy-onefive hundred and seventy-twofive hundred and seventy-threefive hundred and seventy-fourfive hundred and seventy-fivefive hundred and seventy-sixfive hundred and seventy-sevenfive hundred and seventy-eightfive hundred and seventy-ninefive hundred and eightyfive hundred and eighty-onefive hundred and eighty-twofive hundred and eighty-threefive hundred and eighty-fourfive hundred and eighty-fivefive hundred and eighty-sixfive hundred and eighty-sevenfive hundred and eighty-eightfive hundred and eighty-ninefive hundred and ninetyfive hundred and ninety-onefive hundred and ninety-twofive hundred and ninety-threefive hundred and ninety-fourfive hundred and ninety-fivefive hundred and ninety-sixfive hundred and ninety-sevenfive hundred and ninety-eightfive hundred and ninety-ninesix hundredsix hundred and onesix hundred and twosix hundred and threesix hundred and foursix hundred and fivesix hundred and sixsix hundred and sevensix hundred and eightsix hundred and ninesix hundred and tensix hundred and elevensix hundred and twelvesix hundred and thirteensix hundred and fourteensix hundred and fifteensix hundred and sixteensix hundred and seventeensix hundred and eighteensix hundred and nineteensix hundred and twentysix hundred and twenty-onesix hundred and twenty-twosix hundred and twenty-threesix hundred and twenty-foursix hundred and twenty-fivesix hundred and twenty-sixsix hundred and twenty-sevensix hundred and twenty-eightsix hundred and twenty-ninesix hundred and thirtysix hundred and thirty-onesix hundred and thirty-twosix hundred and thirty-threesix hundred and thirty-foursix hundred and thirty-fivesix hundred and thirty-sixsix hundred and thirty-sevensix hundred and thirty-eightsix hundred and thirty-ninesix hundred and fortysix hundred and forty-onesix hundred and forty-twosix hundred and forty-threesix hundred and forty-foursix hundred and forty-fivesix hundred and forty-sixsix hundred and forty-sevensix hundred and forty-eightsix hundred and forty-ninesix hundred and fiftysix hundred and fifty-onesix hundred and fifty-twosix hundred and fifty-threesix hundred and fifty-foursix hundred and fifty-fivesix hundred and fifty-sixsix hundred and fifty-sevensix hundred and fifty-eightsix hundred and fifty-ninesix hundred and sixtysix hundred and sixty-onesix hundred and sixty-twosix hundred and sixty-threesix hundred and sixty-foursix hundred and sixty-fivesix hundred and sixty-sixsix hundred and sixty-sevensix hundred and sixty-eightsix hundred and sixty-ninesix hundred and seventysix hundred and seventy-onesix hundred and seventy-twosix hundred and seventy-threesix hundred and seventy-foursix hundred and seventy-fivesix hundred and seventy-sixsix hundred and seventy-sevensix hundred and seventy-eightsix hundred and seventy-ninesix hundred and eightysix hundred and eighty-onesix hundred and eighty-twosix hundred and eighty-threesix hundred and eighty-foursix hundred and eighty-fivesix hundred and eighty-sixsix hundred and eighty-sevensix hundred and eighty-eightsix hundred and eighty-ninesix hundred and ninetysix hundred and ninety-onesix hundred and ninety-twosix hundred and ninety-threesix hundred and ninety-foursix hundred and ninety-fivesix hundred and ninety-sixsix hundred and ninety-sevensix hundred and ninety-eightsix hundred and ninety-nineseven hundredseven hundred and oneseven hundred and twoseven hundred and threeseven hundred and fourseven hundred and fiveseven hundred and sixseven hundred and sevenseven hundred and eightseven hundred and nineseven hundred and tenseven hundred and elevenseven hundred and twelveseven hundred and thirteenseven hundred and fourteenseven hundred and fifteenseven hundred and sixteenseven hundred and seventeenseven hundred and eighteenseven hundred and nineteenseven hundred and twentyseven hundred and twenty-oneseven hundred and twenty-twoseven hundred and twenty-threeseven hundred and twenty-fourseven hundred and twenty-fiveseven hundred and twenty-sixseven hundred and twenty-sevenseven hundred and twenty-eightseven hundred and twenty-nineseven hundred and thirtyseven hundred and thirty-oneseven hundred and thirty-twoseven hundred and thirty-threeseven hundred and thirty-fourseven hundred and thirty-fiveseven hundred and thirty-sixseven hundred and thirty-sevenseven hundred and thirty-eightseven hundred and thirty-nineseven hundred and fortyseven hundred and forty-oneseven hundred and forty-twoseven hundred and forty-threeseven hundred and forty-fourseven hundred and forty-fiveseven hundred and forty-sixseven hundred and forty-sevenseven hundred and forty-eightseven hundred and forty-nineseven hundred and fiftyseven hundred and fifty-oneseven hundred and fifty-twoseven hundred and fifty-threeseven hundred and fifty-fourseven hundred and fifty-fiveseven hundred and fifty-sixseven hundred and fifty-sevenseven hundred and fifty-eightseven hundred and fifty-nineseven hundred and sixtyseven hundred and sixty-oneseven hundred and sixty-twoseven hundred and sixty-threeseven hundred and sixty-fourseven hundred and sixty-fiveseven hundred and sixty-sixseven hundred and sixty-sevenseven hundred and sixty-eightseven hundred and sixty-nineseven hundred and seventyseven hundred and seventy-oneseven hundred and seventy-twoseven hundred and seventy-threeseven hundred and seventy-fourseven hundred and seventy-fiveseven hundred and seventy-sixseven hundred and seventy-sevenseven hundred and seventy-eightseven hundred and seventy-nineseven hundred and eightyseven hundred and eighty-oneseven hundred and eighty-twoseven hundred and eighty-threeseven hundred and eighty-fourseven hundred and eighty-fiveseven hundred and eighty-sixseven hundred and eighty-sevenseven hundred and eighty-eightseven hundred and eighty-nineseven hundred and ninetyseven hundred and ninety-oneseven hundred and ninety-twoseven hundred and ninety-threeseven hundred and ninety-fourseven hundred and ninety-fiveseven hundred and ninety-sixseven hundred and ninety-sevenseven hundred and ninety-eightseven hundred and ninety-nineeight hundredeight hundred and oneeight hundred and twoeight hundred and threeeight hundred and foureight hundred and fiveeight hundred and sixeight hundred and seveneight hundred and eighteight hundred and nineeight hundred and teneight hundred and eleveneight hundred and twelveeight hundred and thirteeneight hundred and fourteeneight hundred and fifteeneight hundred and sixteeneight hundred and seventeeneight hundred and eighteeneight hundred and nineteeneight hundred and twentyeight hundred and twenty-oneeight hundred and twenty-twoeight hundred and twenty-threeeight hundred and twenty-foureight hundred and twenty-fiveeight hundred and twenty-sixeight hundred and twenty-seveneight hundred and twenty-eighteight hundred and twenty-nineeight hundred and thirtyeight hundred and thirty-oneeight hundred and thirty-twoeight hundred and thirty-threeeight hundred and thirty-foureight hundred and thirty-fiveeight hundred and thirty-sixeight hundred and thirty-seveneight hundred and thirty-eighteight hundred and thirty-nineeight hundred and fortyeight hundred and forty-oneeight hundred and forty-twoeight hundred and forty-threeeight hundred and forty-foureight hundred and forty-fiveeight hundred and forty-sixeight hundred and forty-seveneight hundred and forty-eighteight hundred and forty-nineeight hundred and fiftyeight hundred and fifty-oneeight hundred and fifty-twoeight hundred and fifty-threeeight hundred and fifty-foureight hundred and fifty-fiveeight hundred and fifty-sixeight hundred and fifty-seveneight hundred and fifty-eighteight hundred and fifty-nineeight hundred and sixtyeight hundred and sixty-oneeight hundred and sixty-twoeight hundred and sixty-threeeight hundred and sixty-foureight hundred and sixty-fiveeight hundred and sixty-sixeight hundred and sixty-seveneight hundred and sixty-eighteight hundred and sixty-nineeight hundred and seventyeight hundred and seventy-oneeight hundred and seventy-twoeight hundred and seventy-threeeight hundred and seventy-foureight hundred and seventy-fiveeight hundred and seventy-sixeight hundred and seventy-seveneight hundred and seventy-eighteight hundred and seventy-nineeight hundred and eightyeight hundred and eighty-oneeight hundred and eighty-twoeight hundred and eighty-threeeight hundred and eighty-foureight hundred and eighty-fiveeight hundred and eighty-sixeight hundred and eighty-seveneight hundred and eighty-eighteight hundred and eighty-nineeight hundred and ninetyeight hundred and ninety-oneeight hundred and ninety-twoeight hundred and ninety-threeeight hundred and ninety-foureight hundred and ninety-fiveeight hundred and ninety-sixeight hundred and ninety-seveneight hundred and ninety-eighteight hundred and ninety-ninenine hundrednine hundred and onenine hundred and twonine hundred and threenine hundred and fournine hundred and fivenine hundred and sixnine hundred and sevennine hundred and eightnine hundred and ninenine hundred and tennine hundred and elevennine hundred and twelvenine hundred and thirteennine hundred and fourteennine hundred and fifteennine hundred and sixteennine hundred and seventeennine hundred and eighteennine hundred and nineteennine hundred and twentynine hundred and twenty-onenine hundred and twenty-twonine hundred and twenty-threenine hundred and twenty-fournine hundred and twenty-fivenine hundred and twenty-sixnine hundred and twenty-sevennine hundred and twenty-eightnine hundred and twenty-ninenine hundred and thirtynine hundred and thirty-onenine hundred and thirty-twonine hundred and thirty-threenine hundred and thirty-fournine hundred and thirty-fivenine hundred and thirty-sixnine hundred and thirty-sevennine hundred and thirty-eightnine hundred and thirty-ninenine hundred and fortynine hundred and forty-onenine hundred and forty-twonine hundred and forty-threenine hundred and forty-fournine hundred and forty-fivenine hundred and forty-sixnine hundred and forty-sevennine hundred and forty-eightnine hundred and forty-ninenine hundred and fiftynine hundred and fifty-onenine hundred and fifty-twonine hundred and fifty-threenine hundred and fifty-fournine hundred and fifty-fivenine hundred and fifty-sixnine hundred and fifty-sevennine hundred and fifty-eightnine hundred and fifty-ninenine hundred and sixtynine hundred and sixty-onenine hundred and sixty-twonine hundred and sixty-threenine hundred and sixty-fournine hundred and sixty-fivenine hundred and sixty-sixnine hundred and sixty-sevennine hundred and sixty-eightnine hundred and sixty-ninenine hundred and seventynine hundred and seventy-onenine hundred and seventy-twonine hundred and seventy-threenine hundred and seventy-fournine hundred and seventy-fivenine hundred and seventy-sixnine hundred and seventy-sevennine hundred and seventy-eightnine hundred and seventy-ninenine hundred and eightynine hundred and eighty-onenine hundred and eighty-twonine hundred and eighty-threenine hundred and eighty-fournine hundred and eighty-fivenine hundred and eighty-sixnine hundred and eighty-sevennine hundred and eighty-eightnine hundred and eighty-ninenine hundred and ninetynine hundred and ninety-onenine hundred and ninety-twonine hundred and ninety-threenine hundred and ninety-fournine hundred and ninety-fivenine hundred and ninety-sixnine hundred and ninety-sevennine hundred and ninety-eightnine hundred and ninety-nineone thousand'''
onehundrednumbersasastring = '''onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteentwentytwenty-onetwenty-twotwenty-threetwenty-fourtwenty-fivetwenty-sixtwenty-seventwenty-eighttwenty-ninethirtythirty-onethirty-twothirty-threethirty-fourthirty-fivethirty-sixthirty-seventhirty-eightthirty-ninefortyforty-oneforty-twoforty-threeforty-fourforty-fiveforty-sixforty-sevenforty-eightforty-ninefiftyfifty-onefifty-twofifty-threefifty-fourfifty-fivefifty-sixfifty-sevenfifty-eightfifty-ninesixtysixty-onesixty-twosixty-threesixty-foursixty-fivesixty-sixsixty-sevensixty-eightsixty-nineseventyseventy-oneseventy-twoseventy-threeseventy-fourseventy-fiveseventy-sixseventy-sevenseventy-eightseventy-nineeightyeighty-oneeighty-twoeighty-threeeighty-foureighty-fiveeighty-sixeighty-seveneighty-eighteighty-nineninetyninety-oneninety-twoninety-threeninety-fourninety-fiveninety-sixninety-sevenninety-eightninety-nineone hundred'''
twohundrednumbersasastring = '''onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteentwentytwenty-onetwenty-twotwenty-threetwenty-fourtwenty-fivetwenty-sixtwenty-seventwenty-eighttwenty-ninethirtythirty-onethirty-twothirty-threethirty-fourthirty-fivethirty-sixthirty-seventhirty-eightthirty-ninefortyforty-oneforty-twoforty-threeforty-fourforty-fiveforty-sixforty-sevenforty-eightforty-ninefiftyfifty-onefifty-twofifty-threefifty-fourfifty-fivefifty-sixfifty-sevenfifty-eightfifty-ninesixtysixty-onesixty-twosixty-threesixty-foursixty-fivesixty-sixsixty-sevensixty-eightsixty-nineseventyseventy-oneseventy-twoseventy-threeseventy-fourseventy-fiveseventy-sixseventy-sevenseventy-eightseventy-nineeightyeighty-oneeighty-twoeighty-threeeighty-foureighty-fiveeighty-sixeighty-seveneighty-eighteighty-nineninetyninety-oneninety-twoninety-threeninety-fourninety-fiveninety-sixninety-sevenninety-eightninety-nineone hundredone hundred and oneone hundred and twoone hundred and threeone hundred and fourone hundred and fiveone hundred and sixone hundred and sevenone hundred and eightone hundred and nineone hundred and tenone hundred and elevenone hundred and twelveone hundred and thirteenone hundred and fourteenone hundred and fifteenone hundred and sixteenone hundred and seventeenone hundred and eighteenone hundred and nineteenone hundred and twentyone hundred and twenty-oneone hundred and twenty-twoone hundred and twenty-threeone hundred and twenty-fourone hundred and twenty-fiveone hundred and twenty-sixone hundred and twenty-sevenone hundred and twenty-eightone hundred and twenty-nineone hundred and thirtyone hundred and thirty-oneone hundred and thirty-twoone hundred and thirty-threeone hundred and thirty-fourone hundred and thirty-fiveone hundred and thirty-sixone hundred and thirty-sevenone hundred and thirty-eightone hundred and thirty-nineone hundred and fortyone hundred and forty-oneone hundred and forty-twoone hundred and forty-threeone hundred and forty-fourone hundred and forty-fiveone hundred and forty-sixone hundred and forty-sevenone hundred and forty-eightone hundred and forty-nineone hundred and fiftyone hundred and fifty-oneone hundred and fifty-twoone hundred and fifty-threeone hundred and fifty-fourone hundred and fifty-fiveone hundred and fifty-sixone hundred and fifty-sevenone hundred and fifty-eightone hundred and fifty-nineone hundred and sixtyone hundred and sixty-oneone hundred and sixty-twoone hundred and sixty-threeone hundred and sixty-fourone hundred and sixty-fiveone hundred and sixty-sixone hundred and sixty-sevenone hundred and sixty-eightone hundred and sixty-nineone hundred and seventyone hundred and seventy-oneone hundred and seventy-twoone hundred and seventy-threeone hundred and seventy-fourone hundred and seventy-fiveone hundred and seventy-sixone hundred and seventy-sevenone hundred and seventy-eightone hundred and seventy-nineone hundred and eightyone hundred and eighty-oneone hundred and eighty-twoone hundred and eighty-threeone hundred and eighty-fourone hundred and eighty-fiveone hundred and eighty-sixone hundred and eighty-sevenone hundred and eighty-eightone hundred and eighty-nineone hundred and ninetyone hundred and ninety-oneone hundred and ninety-twoone hundred and ninety-threeone hundred and ninety-fourone hundred and ninety-fiveone hundred and ninety-sixone hundred and ninety-sevenone hundred and ninety-eightone hundred and ninety-ninetwo hundred'''
threehundrednumbersasastring = '''onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteentwentytwenty-onetwenty-twotwenty-threetwenty-fourtwenty-fivetwenty-sixtwenty-seventwenty-eighttwenty-ninethirtythirty-onethirty-twothirty-threethirty-fourthirty-fivethirty-sixthirty-seventhirty-eightthirty-ninefortyforty-oneforty-twoforty-threeforty-fourforty-fiveforty-sixforty-sevenforty-eightforty-ninefiftyfifty-onefifty-twofifty-threefifty-fourfifty-fivefifty-sixfifty-sevenfifty-eightfifty-ninesixtysixty-onesixty-twosixty-threesixty-foursixty-fivesixty-sixsixty-sevensixty-eightsixty-nineseventyseventy-oneseventy-twoseventy-threeseventy-fourseventy-fiveseventy-sixseventy-sevenseventy-eightseventy-nineeightyeighty-oneeighty-twoeighty-threeeighty-foureighty-fiveeighty-sixeighty-seveneighty-eighteighty-nineninetyninety-oneninety-twoninety-threeninety-fourninety-fiveninety-sixninety-sevenninety-eightninety-nineone hundredone hundred and oneone hundred and twoone hundred and threeone hundred and fourone hundred and fiveone hundred and sixone hundred and sevenone hundred and eightone hundred and nineone hundred and tenone hundred and elevenone hundred and twelveone hundred and thirteenone hundred and fourteenone hundred and fifteenone hundred and sixteenone hundred and seventeenone hundred and eighteenone hundred and nineteenone hundred and twentyone hundred and twenty-oneone hundred and twenty-twoone hundred and twenty-threeone hundred and twenty-fourone hundred and twenty-fiveone hundred and twenty-sixone hundred and twenty-sevenone hundred and twenty-eightone hundred and twenty-nineone hundred and thirtyone hundred and thirty-oneone hundred and thirty-twoone hundred and thirty-threeone hundred and thirty-fourone hundred and thirty-fiveone hundred and thirty-sixone hundred and thirty-sevenone hundred and thirty-eightone hundred and thirty-nineone hundred and fortyone hundred and forty-oneone hundred and forty-twoone hundred and forty-threeone hundred and forty-fourone hundred and forty-fiveone hundred and forty-sixone hundred and forty-sevenone hundred and forty-eightone hundred and forty-nineone hundred and fiftyone hundred and fifty-oneone hundred and fifty-twoone hundred and fifty-threeone hundred and fifty-fourone hundred and fifty-fiveone hundred and fifty-sixone hundred and fifty-sevenone hundred and fifty-eightone hundred and fifty-nineone hundred and sixtyone hundred and sixty-oneone hundred and sixty-twoone hundred and sixty-threeone hundred and sixty-fourone hundred and sixty-fiveone hundred and sixty-sixone hundred and sixty-sevenone hundred and sixty-eightone hundred and sixty-nineone hundred and seventyone hundred and seventy-oneone hundred and seventy-twoone hundred and seventy-threeone hundred and seventy-fourone hundred and seventy-fiveone hundred and seventy-sixone hundred and seventy-sevenone hundred and seventy-eightone hundred and seventy-nineone hundred and eightyone hundred and eighty-oneone hundred and eighty-twoone hundred and eighty-threeone hundred and eighty-fourone hundred and eighty-fiveone hundred and eighty-sixone hundred and eighty-sevenone hundred and eighty-eightone hundred and eighty-nineone hundred and ninetyone hundred and ninety-oneone hundred and ninety-twoone hundred and ninety-threeone hundred and ninety-fourone hundred and ninety-fiveone hundred and ninety-sixone hundred and ninety-sevenone hundred and ninety-eightone hundred and ninety-ninetwo hundredtwo hundred and onetwo hundred and twotwo hundred and threetwo hundred and fourtwo hundred and fivetwo hundred and sixtwo hundred and seventwo hundred and eighttwo hundred and ninetwo hundred and tentwo hundred and eleventwo hundred and twelvetwo hundred and thirteentwo hundred and fourteentwo hundred and fifteentwo hundred and sixteentwo hundred and seventeentwo hundred and eighteentwo hundred and nineteentwo hundred and twentytwo hundred and twenty-onetwo hundred and twenty-twotwo hundred and twenty-threetwo hundred and twenty-fourtwo hundred and twenty-fivetwo hundred and twenty-sixtwo hundred and twenty-seventwo hundred and twenty-eighttwo hundred and twenty-ninetwo hundred and thirtytwo hundred and thirty-onetwo hundred and thirty-twotwo hundred and thirty-threetwo hundred and thirty-fourtwo hundred and thirty-fivetwo hundred and thirty-sixtwo hundred and thirty-seventwo hundred and thirty-eighttwo hundred and thirty-ninetwo hundred and fortytwo hundred and forty-onetwo hundred and forty-twotwo hundred and forty-threetwo hundred and forty-fourtwo hundred and forty-fivetwo hundred and forty-sixtwo hundred and forty-seventwo hundred and forty-eighttwo hundred and forty-ninetwo hundred and fiftytwo hundred and fifty-onetwo hundred and fifty-twotwo hundred and fifty-threetwo hundred and fifty-fourtwo hundred and fifty-fivetwo hundred and fifty-sixtwo hundred and fifty-seventwo hundred and fifty-eighttwo hundred and fifty-ninetwo hundred and sixtytwo hundred and sixty-onetwo hundred and sixty-twotwo hundred and sixty-threetwo hundred and sixty-fourtwo hundred and sixty-fivetwo hundred and sixty-sixtwo hundred and sixty-seventwo hundred and sixty-eighttwo hundred and sixty-ninetwo hundred and seventytwo hundred and seventy-onetwo hundred and seventy-twotwo hundred and seventy-threetwo hundred and seventy-fourtwo hundred and seventy-fivetwo hundred and seventy-sixtwo hundred and seventy-seventwo hundred and seventy-eighttwo hundred and seventy-ninetwo hundred and eightytwo hundred and eighty-onetwo hundred and eighty-twotwo hundred and eighty-threetwo hundred and eighty-fourtwo hundred and eighty-fivetwo hundred and eighty-sixtwo hundred and eighty-seventwo hundred and eighty-eighttwo hundred and eighty-ninetwo hundred and ninetytwo hundred and ninety-onetwo hundred and ninety-twotwo hundred and ninety-threetwo hundred and ninety-fourtwo hundred and ninety-fivetwo hundred and ninety-sixtwo hundred and ninety-seventwo hundred and ninety-eighttwo hundred and ninety-ninethree hundred'''

import re,string, collections
def euler017(t = euler017Data):
    pattern = re.compile('[\W]+')
    t = pattern.sub('',t)
    return len(t)


def euler030limit():
    i = 1
    while(True):
        if(9**i > i* 9**5):
            return 9**i
        i += 1

def euler030(power = 5, enditers = euler030limit()):
    accum = 0
    for i in range(enditers):
        a = 0
        for d in str(i):
            a += int(d)**power
        if a == i:
            print (a)
            accum += a
    return accum - 1

def euler019(beginYear=1901, endYear = 2000):
    '''2011-07-20-1658'''
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    assert sum(days)==365
    day = 1
    #month = 0
    year = beginYear
    sundays = 0
    while True:
        for month in range(12):
            if day%7 == 0:
                sundays +=1
            if month == 1 and year % 400 != 0:
                day += 29
            else:
                day += days[month]
        year += 1
        if(year > endYear):
            print (day,month,year)
            return sundays

def euler029(end = 100):
    s = set()
    for a in range(2,end+1):
        for b in range(2,end+1):
            s.add(a**b)
    return len(s)

def euler023(upperlimit = 28123):
    '''2011-07-21-1814
    finish 1836'''
    #find all abundant numbers less than 28123
    aNums = []
    for n in range(12,upperlimit):
        if abundantNumber(n):
            aNums.append(n)
    sums = []
    for c in combinations_with_replacement(aNums,2):
        sums.append(sum(c))
    
    ans = frozenset(range(1,upperlimit)).difference(frozenset(sums))
    return sum(ans)

def reciprocalDecimalPeriodLength(n):
    '''formula from some fucking place
    it doesn't work for multiples of 2 or 5
    I don't understand it.'''
    k = 1
    if (n%2 != 0 and n%5 != 0):
        while True:
            if ((10**k)-1) %n == 0:
                #print (k)
                return k
            #print (k, 10**k-1, (10**k-1) %n)
            k+=1
    return 1

def euler026(n = 1000):
    ''''''
    maxi = 1
    maxn = 0
    for d in range(1,n):
        if reciprocalDecimalPeriodLength(d) > maxi:
            maxi = reciprocalDecimalPeriodLength(d)
            maxn = d
    return maxn

assert euler026() == 983

def euler020(n = 100):
    return sum([int(c) for c in str(math.factorial(n))])

def isPalindrome(n):
    s = str(n)
    for i,c in enumerate(s):
        if s[i] != s[-(i+1)]:
            return False
    return True

def euler004():
    ps = []
    for a in range(999,99,-1):
        for b in range(a,99,-1):
            if isPalindrome(a*b):
                ps.append((a*b,a,b))
    return max(ps)

def numberRotations(n):
    '''returns rotations of the number passed in
    >>> numberRotations(719)
    [719, 971, 197]
    '''
    s = str(n)
    l= len(s)
    return [int("".join([s[i-j] for i in range(l)])) for j in range(l)]

pTable = set()

def isPrime(n):
    global pTable
    if n in pTable: return True
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    pTable.add(n)
    return True

assert isPrime(1) == False
assert isPrime(2) == True
assert isPrime(3) == True
assert isPrime(4) == False
assert isPrime(5) == True
assert isPrime(6) == False
assert isPrime(7) == True


def containsEvens(n):
    r = re.compile('[02468]')
    if r.search(str(n)) is None:
        return False
    return True

def circularPrime(n):
    rots = numberRotations(n)
    if containsEvens(n):
        return False
    return all([isPrime(n) for n in rots])
    
def euler035(limit = 1000000):
    '''solved 2011-07-22-1541
    finished in approximately a hour'''
    cp = set()
    cp.add(2)
    for i in range (3,limit,2):
        if i not in cp and circularPrime(i):
            cp.update(numberRotations(i))
        #print(cp)
    print(len(cp),sum(cp))
    return cp

def pandigitalNumber(i):
    #print('enter pandigital',i, log10(float(i)))
    #n = ceil(log10(float(i)))
    n = ceil(log10(i))
    if all([c in str(i) for c in [str(a) for a in range(1,n+1)]]):
            return True
    return False

def pandigitalPrime(n):
    if pandigitalNumber(n) and isPrime(n):
        return True
    return False


def euler041(limit = 7):
    '''finished 1630
    ~30min
    from divisibility rules
    if the digits of a number are divisible by 3, the number is divisible by 3
    for bothe 8 and 9 length pandigital numbers, the sum is divisible by 3,
    thus those are all composite and not prime, so we need not check them.
    [print('Sum of numbers from 1 to ' + str(n)+': ' + str(sum(range(1,n+1)))) for n in range(9,0,-1)]
    Sum of numbers from 1 to 9: 45
    Sum of numbers from 1 to 8: 36
    Sum of numbers from 1 to 7: 28
    Sum of numbers from 1 to 6: 21
    Sum of numbers from 1 to 5: 15
    Sum of numbers from 1 to 4: 10
    Sum of numbers from 1 to 3: 6
    Sum of numbers from 1 to 2: 3
    Sum of numbers from 1 to 1: 1
    '''
    l = []
    for top in range(limit,1,-1):
        for n in permutations([str(a) for a in range(top,0,-1)],top):
            c = int("".join(n))
            if (isPrime(c)):
                return c
                #print(c,pandigitalPrime(c))
                l.append(c)
    return max(l)            

def leftTruncations(n):
    s = str(n)
    l= len(s)
    return [int(s[i:]) for i in range(l)]

def rightTruncations(n):
    t = []
    while n > 0:
        t.append(n)
        n //=10
    return t

def allPrime(l):
    return all([isPrime(n) for n in l])

def euler037(limit = 11):
    lrt = []
    i = 11
    while len(lrt) < limit:
        if (allPrime(leftTruncations(i)) and allPrime(rightTruncations(i))):
            lrt.append(i)
            print (i)
        i+=2
    return lrt

def euler097():
    return (28433*pow(2,7830457,10**10)+1)%10**10
assert euler097() == 8739992577

def primeSieve(below = 2):
    primes = []
    if below < 3:
        return primes
    if below > 2:
        primes += [2]
    if below > 3:
        primes += [3]
    return primes

def sieveErasthones(below = 2):
    return []


def timePowers(iters = 10):
    s = '''
    for i in range(46340):
        x = i*i
    '''
    t = Timer(s)
    print(t.repeat(3,iters))
    s = '''
    for i in range(46340):
        x = i**2
    '''
    t = Timer(s)
    print(t.repeat(3,iters))
    s = '''
    for i in range(46340):
        x = pow(i,2)
    '''
    t = Timer(s)
    print(t.repeat(3,iters))

def haywardPrimeSieve2to3(upTo):
    primes = [2,3]
    k1 = int(math.ceil((upTo-1)/6))
    k2 = int(math.ceil((upTo+1)/6))
    temp1 = dict((n*6-1, n*6-1) for n in range(1,k2))
    temp2 = dict((n*6+1, n*6+1) for n in range(1,k1))
    numbers = dict(list(temp1.items()) + list(temp2.items()))
    temp1 = None
    temp2 = None
    #print (k1, k2, temp1, temp2, numbers)
    i = 1
    while i not in numbers:
            i+=1
    while i**2 < upTo:
        #print numbers
        number = i       
        primes = primes + [number]
        s = set()
        for value in numbers:
            #remove the multiples of value
            if number*value < upTo:
                s.add(number*value)
        for v in s:
            del numbers[v]
        del numbers[number]
        while i not in numbers:
            i+=1
    for v in numbers:
        primes.append(v)
    primes.sort()
    return primes

def haywardPrimeSievePy3k(upTo):
    primes = [2,3]
    k1 = int(math.ceil((upTo-1)/6))
    k2 = int(math.ceil((upTo+1)/6))
    temp1 = dict((n*6-1, n*6-1) for n in range(1,k2))
    temp2 = dict((n*6+1, n*6+1) for n in range(1,k1))
    temp1.update(temp2)
    numbers = temp1
    temp1 = None
    temp2 = None
    #print (k1, k2, temp1, temp2, numbers)
    i = 1
    while i not in numbers:
            i+=1
    while i**2 < upTo:
        #print numbers
        number = i       
        primes = primes + [number]
        s = set()
        for value in numbers:
            #remove the multiples of value
            if number*value < upTo:
                s.add(number*value)
        for v in s:
            del numbers[v]
        del numbers[number]
        while i not in numbers:
            i+=1
    for v in numbers:
        primes.append(v)
    primes.sort()
    return primes

def haywardPrimeSieveSet(below = 15):
    primes = []
    if below < 3:
        return primes
    if below > 2:
        primes += [2]
    if below > 3:
        primes += [3]
    if below > 5:
        k1 = int(math.ceil((below-1)/6))
        k2 = int(math.ceil((below+1)/6))
        numbers = {y*6+1 for y in range(1,k1)}.union({x*6-1 for x in range(1,k2)})
        #print (k1, k2, numbers)
        i = 5
        while i*i < below:
            #print (list(numbers)) 
            primes = primes + [i]
            s = set()
            for value in numbers:
                x = i*value
                if x < below:
                    s.add(x)
            s.add(i)
            numbers.difference_update(s)
            #for v in s:
            #    numbers.remove(v)
            #numbers.remove(i)
            i+=2
            while i not in numbers:
                i+=2
        for v in numbers:
            primes.append(v)
        primes.sort()
    return primes

def haywardPrimeSieveSetIndex(below = 15):
    primes = []
    if below < 3:
        return primes
    if below > 2:
        primes += [2]
    if below > 3:
        primes += [3]
    if below > 5:
        k1 = int(math.ceil((below-1)/6))
        k2 = int(math.ceil((below+1)/6))
        temp1 = {n*6-1 for n in range(1,k2)}
        temp2 = {n*6+1 for n in range(1,k1)}
        numbers = temp1.union(temp2)
        temp1 = None
        temp2 = None
        #print (k1, k2, temp1, temp2, numbers)
        i = 5
        while i*i < below:
            #print (list(numbers)) 
            primes = primes + [i]
            s = set()
            for value in numbers:
                if i*value < below:
                    s.add(i*value)
            numbers.difference_update(s)
##            for v in s:
##                numbers.remove(v)
            numbers.remove(i)
            i+=1
            while i not in numbers:
                i+=1
        for v in numbers:
            primes.append(v)
        primes.sort()
    return primes

def haywardPrimeSieveSetMin(upTo = 15):
    primes = [2,3]
    k1 = int(math.ceil((upTo-1)/6))
    k2 = int(math.ceil((upTo+1)/6))
    temp1 = {n*6-1 for n in range(1,k2)}
    temp2 = {n*6+1 for n in range(1,k1)}
    numbers = temp1.union(temp2)
    temp1 = None
    temp2 = None
    #print (k1, k2, temp1, temp2, numbers)
    i = 1
    while i not in numbers:
        i+=1
    while i*i < upTo:
        #print (list(numbers))
        primes = primes + [i]
        s = set()
        for value in numbers:
            if i*value < upTo:
                s.add(i*value)
        for v in s:
            numbers.remove(v)
        numbers.remove(i)
        i = min(numbers)
    for v in numbers:
        primes.append(v)
    primes.sort()
    return primes

def haywardPrimeSieveSetListSort(upTo = 15):
    primes = [2,3]
    k1 = int(math.ceil((upTo-1)/6))
    k2 = int(math.ceil((upTo+1)/6))
    temp1 = {n*6-1 for n in range(1,k2)}
    temp2 = {n*6+1 for n in range(1,k1)}
    numbers = temp1.union(temp2)
    temp1 = None
    temp2 = None
    #print (k1, k2, temp1, temp2, numbers)
    i = 1
    while i not in numbers:
        i+=1
    while i*i < upTo:
        #print (list(numbers))
        number = i       
        primes = primes + [number]
        s = set()
        n = list(numbers)
        n.sort()
        for value in n:
            if number*value < upTo:
                s.add(number*value)
            else:
                break
        for v in s:
            numbers.remove(v)
        numbers.remove(number)
        while i not in numbers:
            i+=1
    for v in numbers:
        primes.append(v)
    primes.sort()
    return primes

def primeSieve1(upTo):
    primes = [2,3]
    k1 = int(math.ceil((upTo-1)/6))
    k2 = int(math.ceil((upTo+1)/6))
    temp1 = dict((n*6-1, n*6-1) for n in range(1,k2))
    temp2 = dict((n*6+1, n*6+1) for n in range(1,k1))
    temp1.update(temp2)
    numbers = temp1
    temp1 = None
    temp2 = None
    #print k1, k2, temp1, temp2, numbers
    i = 1
    while i not in numbers:
        i+=1
    while i**2 < upTo:
        number = i
        primes = primes + [number]
        #print (numbers)
        #print (range(number,upTo, number*2))
        for value in range(number, upTo, number*2):
           if value in numbers:
               del numbers[value]
        while i not in numbers:
           i+=2
    primes.extend([v for v in numbers])
       
    primes.sort()
    return primes

def primeSieve2(upTo):
    primes = [2,3]
    k1 = int(math.ceil((upTo-1)/6))
    k2 = int(math.ceil((upTo+1)/6))
    numbers = {y*6+1 for y in range(1,k1)}.union({x*6-1 for x in range(1,k2)})
    i = 1
    while i not in numbers:
        i+=1
    while i**2 < upTo:
        number = i
        primes = primes + [number]
        for value in range(number, upTo, number*2):
           if value in numbers:
               numbers.remove(value)
        i+=2
        while i not in numbers:
           i+=2
    for v in numbers:
       primes.append(v)
    primes.sort()
    return primes

def gen_sieve(ceiling=None):
    if ceiling is not None:
        if ceiling % 2 == 0:
            ceiling -= 1
        highest_prime = math.ceil(math.sqrt(ceiling))
    last_val = 1
    found_primes = []
    yield 2
    while ceiling is None or ceiling > last_val:
        current_val = None
        while current_val is None:
            current_val = last_val = last_val + 2
            for prime, square in found_primes:
                if current_val < square: 
                    break
                if current_val % prime == 0:
                    current_val = None
                    break
        yield current_val
        if ceiling is None or highest_prime > last_val:
            found_primes.append((current_val, current_val ** 2))
   
def SieveTest(below = 100):
    pset = primeSieve2(below)
    pPy3k = list(gen_sieve(below-2))
    #print(pset)
    #print(pPy3k)
    assert len(pset) == len(pPy3k)
    assert all([ x == y for (x,y) in zip(pset,pPy3k)])
    return all([isPrime(n) for n in pset])



def timePrimeSieve():
    setup = '''import MorganEuler
import imp
imp.reload(MorganEuler)'''
    t = Timer("ps = MorganEuler.haywardPrimeSieve2to3(100000)", setup)
    print(t.repeat(3,3))
    t = Timer("ps = MorganEuler.primeSieve1(10000000)", setup)
    print(t.repeat(3,1))
    t = Timer("ps = MorganEuler.primeSieve2(10000000)", setup)
    print(t.repeat(3,1))
    t = Timer("ps = list(MorganEuler.gen_sieve(1000000-2))", setup)
    print(t.repeat(3,1))
        
def euler027(limit = 1000):
    '''finished 2011-07-27-2040'''
    ps = frozenset(primeSieve2(2000000))
    bprimes = primeSieve2(1000)
    bprimes.reverse()
    m = 0
    maxcoeffs = (0,0)
    for a in range (-(limit-1),limit):
        #print(a)
        for b in bprimes:
            n = 0
            expr = (n*n)+(a*n)+b
            #print(expr)
            while expr > 0 and expr in ps:
                n+=1
                expr = (n*n)+(a*n)+b            
            if n > m:
                print(m,n,a,b,maxcoeffs)
                m = n
                maxcoeffs = (a,b)
    return (m,maxcoeffs)

def firstAvailable(numKinds):
    tbl = [1,2,5,10,20,50,100,200]
    return tbl[numKinds-1]

recurse = 0

def cc(amt, kinds):
    global recurse
    recurse += 1
    if amt == 0:
        return 1
    if amt < 0 or kinds == 0:
        return 0
    return cc(amt, kinds-1) + cc(amt-firstAvailable(kinds), kinds)

def euler031():
    return cc(200,8)

def euler032(limit = 9):
    '''
    instead of brute force
    from product, do divisors
    '''
    products = set()
    for n in permutations('123456789'):
        for i in range(1,6):
            for j in range(1,9-i):
                a = ''.join(n[0:i])
                b = ''.join(n[i:i+j])
                c = ''.join(n[i+j:])
                #print(a,b,c)
                if(int(a)*int(b) == int(c)):
                    products.add(int(c))
    return sum(products)
                    
def euler038():
    m = 0
    for i in range(9123,9999):
        pan = int(str(i)+str(i*2))
        if pan< 10**9 and pandigitalNumber(pan) and pan > m:
            m = pan
    return m

def isLychrel(n):
    for i in range(50):
        n = n + int(str(n)[::-1])
        #print(n)
        if(isPalindrome(n)):
            return False
    return True

def euler055(limit = 10000):
    '''start 2011-07-28-2138
    finished ~10 min later'''
    count = 0
    for n in range (limit):
        if isLychrel(n):
            count +=1
    return count

def euler063():
    count = 0
    for base in range(1,10):
        for power in range(0,400):
            if len(str(base**power)) == power:
                print (base**power)
                count +=1
    return count

def euler044(limit = 3000):
    Ds = []
    pents = [pentagonalNumber(i) for i in range(1,limit)]
    pentSet = frozenset(pents)
    for i in pents:
        for j in pents:
            #i = pentagonalNumber(x)
            #j = pentagonalNumber(y)
            if i!= j and (i+j in pentSet) and (abs(i-j) in pentSet):
                Ds.append((abs(i-j), i,j))
    return min(Ds)


def euler047(consec = 4):
    '''finished at 2011-07-28-2257'''
    count = 0
    i = 1
    while count < consec:
        for n in range(i,i+consec):
            if len(primeFactors(n)) != consec:
                count = 0
                break
            else:
                count += 1
        i+= 1
    return i-1

def producet(l):
    return reduce(lambda x,y: x*y, l)

def euler033():
    '''finished before 2011-07-29-1836'''
    fracs = []
    for numer in range(10,100):
        for denom in range(numer+1,100):
            newNum = int(str(numer)[0])
            newDenom = int(str(denom)[1])
            if newDenom != 0 and str(numer)[1] == str(denom)[0] and numer/denom == newNum/newDenom:
                fracs.append(Fraction(numer,denom))
    return reduce(lambda x,y: x*y, fracs).denominator

def factorialSumDigits(n):
    return n == sum([math.factorial(int(d)) for d in str(n)])

def euler034(limit= 100000):
    accum = 0
    for i in range(3,limit):
        if factorialSumDigits(i):
            accum+=i
    return accum

fourtyTwoText = ["A","ABILITY","ABLE","ABOUT","ABOVE","ABSENCE","ABSOLUTELY","ACADEMIC","ACCEPT","ACCESS","ACCIDENT","ACCOMPANY","ACCORDING","ACCOUNT","ACHIEVE","ACHIEVEMENT","ACID","ACQUIRE","ACROSS","ACT","ACTION","ACTIVE","ACTIVITY","ACTUAL","ACTUALLY","ADD","ADDITION","ADDITIONAL","ADDRESS","ADMINISTRATION","ADMIT","ADOPT","ADULT","ADVANCE","ADVANTAGE","ADVICE","ADVISE","AFFAIR","AFFECT","AFFORD","AFRAID","AFTER","AFTERNOON","AFTERWARDS","AGAIN","AGAINST","AGE","AGENCY","AGENT","AGO","AGREE","AGREEMENT","AHEAD","AID","AIM","AIR","AIRCRAFT","ALL","ALLOW","ALMOST","ALONE","ALONG","ALREADY","ALRIGHT","ALSO","ALTERNATIVE","ALTHOUGH","ALWAYS","AMONG","AMONGST","AMOUNT","AN","ANALYSIS","ANCIENT","AND","ANIMAL","ANNOUNCE","ANNUAL","ANOTHER","ANSWER","ANY","ANYBODY","ANYONE","ANYTHING","ANYWAY","APART","APPARENT","APPARENTLY","APPEAL","APPEAR","APPEARANCE","APPLICATION","APPLY","APPOINT","APPOINTMENT","APPROACH","APPROPRIATE","APPROVE","AREA","ARGUE","ARGUMENT","ARISE","ARM","ARMY","AROUND","ARRANGE","ARRANGEMENT","ARRIVE","ART","ARTICLE","ARTIST","AS","ASK","ASPECT","ASSEMBLY","ASSESS","ASSESSMENT","ASSET","ASSOCIATE","ASSOCIATION","ASSUME","ASSUMPTION","AT","ATMOSPHERE","ATTACH","ATTACK","ATTEMPT","ATTEND","ATTENTION","ATTITUDE","ATTRACT","ATTRACTIVE","AUDIENCE","AUTHOR","AUTHORITY","AVAILABLE","AVERAGE","AVOID","AWARD","AWARE","AWAY","AYE","BABY","BACK","BACKGROUND","BAD","BAG","BALANCE","BALL","BAND","BANK","BAR","BASE","BASIC","BASIS","BATTLE","BE","BEAR","BEAT","BEAUTIFUL","BECAUSE","BECOME","BED","BEDROOM","BEFORE","BEGIN","BEGINNING","BEHAVIOUR","BEHIND","BELIEF","BELIEVE","BELONG","BELOW","BENEATH","BENEFIT","BESIDE","BEST","BETTER","BETWEEN","BEYOND","BIG","BILL","BIND","BIRD","BIRTH","BIT","BLACK","BLOCK","BLOOD","BLOODY","BLOW","BLUE","BOARD","BOAT","BODY","BONE","BOOK","BORDER","BOTH","BOTTLE","BOTTOM","BOX","BOY","BRAIN","BRANCH","BREAK","BREATH","BRIDGE","BRIEF","BRIGHT","BRING","BROAD","BROTHER","BUDGET","BUILD","BUILDING","BURN","BUS","BUSINESS","BUSY","BUT","BUY","BY","CABINET","CALL","CAMPAIGN","CAN","CANDIDATE","CAPABLE","CAPACITY","CAPITAL","CAR","CARD","CARE","CAREER","CAREFUL","CAREFULLY","CARRY","CASE","CASH","CAT","CATCH","CATEGORY","CAUSE","CELL","CENTRAL","CENTRE","CENTURY","CERTAIN","CERTAINLY","CHAIN","CHAIR","CHAIRMAN","CHALLENGE","CHANCE","CHANGE","CHANNEL","CHAPTER","CHARACTER","CHARACTERISTIC","CHARGE","CHEAP","CHECK","CHEMICAL","CHIEF","CHILD","CHOICE","CHOOSE","CHURCH","CIRCLE","CIRCUMSTANCE","CITIZEN","CITY","CIVIL","CLAIM","CLASS","CLEAN","CLEAR","CLEARLY","CLIENT","CLIMB","CLOSE","CLOSELY","CLOTHES","CLUB","COAL","CODE","COFFEE","COLD","COLLEAGUE","COLLECT","COLLECTION","COLLEGE","COLOUR","COMBINATION","COMBINE","COME","COMMENT","COMMERCIAL","COMMISSION","COMMIT","COMMITMENT","COMMITTEE","COMMON","COMMUNICATION","COMMUNITY","COMPANY","COMPARE","COMPARISON","COMPETITION","COMPLETE","COMPLETELY","COMPLEX","COMPONENT","COMPUTER","CONCENTRATE","CONCENTRATION","CONCEPT","CONCERN","CONCERNED","CONCLUDE","CONCLUSION","CONDITION","CONDUCT","CONFERENCE","CONFIDENCE","CONFIRM","CONFLICT","CONGRESS","CONNECT","CONNECTION","CONSEQUENCE","CONSERVATIVE","CONSIDER","CONSIDERABLE","CONSIDERATION","CONSIST","CONSTANT","CONSTRUCTION","CONSUMER","CONTACT","CONTAIN","CONTENT","CONTEXT","CONTINUE","CONTRACT","CONTRAST","CONTRIBUTE","CONTRIBUTION","CONTROL","CONVENTION","CONVERSATION","COPY","CORNER","CORPORATE","CORRECT","COS","COST","COULD","COUNCIL","COUNT","COUNTRY","COUNTY","COUPLE","COURSE","COURT","COVER","CREATE","CREATION","CREDIT","CRIME","CRIMINAL","CRISIS","CRITERION","CRITICAL","CRITICISM","CROSS","CROWD","CRY","CULTURAL","CULTURE","CUP","CURRENT","CURRENTLY","CURRICULUM","CUSTOMER","CUT","DAMAGE","DANGER","DANGEROUS","DARK","DATA","DATE","DAUGHTER","DAY","DEAD","DEAL","DEATH","DEBATE","DEBT","DECADE","DECIDE","DECISION","DECLARE","DEEP","DEFENCE","DEFENDANT","DEFINE","DEFINITION","DEGREE","DELIVER","DEMAND","DEMOCRATIC","DEMONSTRATE","DENY","DEPARTMENT","DEPEND","DEPUTY","DERIVE","DESCRIBE","DESCRIPTION","DESIGN","DESIRE","DESK","DESPITE","DESTROY","DETAIL","DETAILED","DETERMINE","DEVELOP","DEVELOPMENT","DEVICE","DIE","DIFFERENCE","DIFFERENT","DIFFICULT","DIFFICULTY","DINNER","DIRECT","DIRECTION","DIRECTLY","DIRECTOR","DISAPPEAR","DISCIPLINE","DISCOVER","DISCUSS","DISCUSSION","DISEASE","DISPLAY","DISTANCE","DISTINCTION","DISTRIBUTION","DISTRICT","DIVIDE","DIVISION","DO","DOCTOR","DOCUMENT","DOG","DOMESTIC","DOOR","DOUBLE","DOUBT","DOWN","DRAW","DRAWING","DREAM","DRESS","DRINK","DRIVE","DRIVER","DROP","DRUG","DRY","DUE","DURING","DUTY","EACH","EAR","EARLY","EARN","EARTH","EASILY","EAST","EASY","EAT","ECONOMIC","ECONOMY","EDGE","EDITOR","EDUCATION","EDUCATIONAL","EFFECT","EFFECTIVE","EFFECTIVELY","EFFORT","EGG","EITHER","ELDERLY","ELECTION","ELEMENT","ELSE","ELSEWHERE","EMERGE","EMPHASIS","EMPLOY","EMPLOYEE","EMPLOYER","EMPLOYMENT","EMPTY","ENABLE","ENCOURAGE","END","ENEMY","ENERGY","ENGINE","ENGINEERING","ENJOY","ENOUGH","ENSURE","ENTER","ENTERPRISE","ENTIRE","ENTIRELY","ENTITLE","ENTRY","ENVIRONMENT","ENVIRONMENTAL","EQUAL","EQUALLY","EQUIPMENT","ERROR","ESCAPE","ESPECIALLY","ESSENTIAL","ESTABLISH","ESTABLISHMENT","ESTATE","ESTIMATE","EVEN","EVENING","EVENT","EVENTUALLY","EVER","EVERY","EVERYBODY","EVERYONE","EVERYTHING","EVIDENCE","EXACTLY","EXAMINATION","EXAMINE","EXAMPLE","EXCELLENT","EXCEPT","EXCHANGE","EXECUTIVE","EXERCISE","EXHIBITION","EXIST","EXISTENCE","EXISTING","EXPECT","EXPECTATION","EXPENDITURE","EXPENSE","EXPENSIVE","EXPERIENCE","EXPERIMENT","EXPERT","EXPLAIN","EXPLANATION","EXPLORE","EXPRESS","EXPRESSION","EXTEND","EXTENT","EXTERNAL","EXTRA","EXTREMELY","EYE","FACE","FACILITY","FACT","FACTOR","FACTORY","FAIL","FAILURE","FAIR","FAIRLY","FAITH","FALL","FAMILIAR","FAMILY","FAMOUS","FAR","FARM","FARMER","FASHION","FAST","FATHER","FAVOUR","FEAR","FEATURE","FEE","FEEL","FEELING","FEMALE","FEW","FIELD","FIGHT","FIGURE","FILE","FILL","FILM","FINAL","FINALLY","FINANCE","FINANCIAL","FIND","FINDING","FINE","FINGER","FINISH","FIRE","FIRM","FIRST","FISH","FIT","FIX","FLAT","FLIGHT","FLOOR","FLOW","FLOWER","FLY","FOCUS","FOLLOW","FOLLOWING","FOOD","FOOT","FOOTBALL","FOR","FORCE","FOREIGN","FOREST","FORGET","FORM","FORMAL","FORMER","FORWARD","FOUNDATION","FREE","FREEDOM","FREQUENTLY","FRESH","FRIEND","FROM","FRONT","FRUIT","FUEL","FULL","FULLY","FUNCTION","FUND","FUNNY","FURTHER","FUTURE","GAIN","GAME","GARDEN","GAS","GATE","GATHER","GENERAL","GENERALLY","GENERATE","GENERATION","GENTLEMAN","GET","GIRL","GIVE","GLASS","GO","GOAL","GOD","GOLD","GOOD","GOVERNMENT","GRANT","GREAT","GREEN","GREY","GROUND","GROUP","GROW","GROWING","GROWTH","GUEST","GUIDE","GUN","HAIR","HALF","HALL","HAND","HANDLE","HANG","HAPPEN","HAPPY","HARD","HARDLY","HATE","HAVE","HE","HEAD","HEALTH","HEAR","HEART","HEAT","HEAVY","HELL","HELP","HENCE","HER","HERE","HERSELF","HIDE","HIGH","HIGHLY","HILL","HIM","HIMSELF","HIS","HISTORICAL","HISTORY","HIT","HOLD","HOLE","HOLIDAY","HOME","HOPE","HORSE","HOSPITAL","HOT","HOTEL","HOUR","HOUSE","HOUSEHOLD","HOUSING","HOW","HOWEVER","HUGE","HUMAN","HURT","HUSBAND","I","IDEA","IDENTIFY","IF","IGNORE","ILLUSTRATE","IMAGE","IMAGINE","IMMEDIATE","IMMEDIATELY","IMPACT","IMPLICATION","IMPLY","IMPORTANCE","IMPORTANT","IMPOSE","IMPOSSIBLE","IMPRESSION","IMPROVE","IMPROVEMENT","IN","INCIDENT","INCLUDE","INCLUDING","INCOME","INCREASE","INCREASED","INCREASINGLY","INDEED","INDEPENDENT","INDEX","INDICATE","INDIVIDUAL","INDUSTRIAL","INDUSTRY","INFLUENCE","INFORM","INFORMATION","INITIAL","INITIATIVE","INJURY","INSIDE","INSIST","INSTANCE","INSTEAD","INSTITUTE","INSTITUTION","INSTRUCTION","INSTRUMENT","INSURANCE","INTEND","INTENTION","INTEREST","INTERESTED","INTERESTING","INTERNAL","INTERNATIONAL","INTERPRETATION","INTERVIEW","INTO","INTRODUCE","INTRODUCTION","INVESTIGATE","INVESTIGATION","INVESTMENT","INVITE","INVOLVE","IRON","IS","ISLAND","ISSUE","IT","ITEM","ITS","ITSELF","JOB","JOIN","JOINT","JOURNEY","JUDGE","JUMP","JUST","JUSTICE","KEEP","KEY","KID","KILL","KIND","KING","KITCHEN","KNEE","KNOW","KNOWLEDGE","LABOUR","LACK","LADY","LAND","LANGUAGE","LARGE","LARGELY","LAST","LATE","LATER","LATTER","LAUGH","LAUNCH","LAW","LAWYER","LAY","LEAD","LEADER","LEADERSHIP","LEADING","LEAF","LEAGUE","LEAN","LEARN","LEAST","LEAVE","LEFT","LEG","LEGAL","LEGISLATION","LENGTH","LESS","LET","LETTER","LEVEL","LIABILITY","LIBERAL","LIBRARY","LIE","LIFE","LIFT","LIGHT","LIKE","LIKELY","LIMIT","LIMITED","LINE","LINK","LIP","LIST","LISTEN","LITERATURE","LITTLE","LIVE","LIVING","LOAN","LOCAL","LOCATION","LONG","LOOK","LORD","LOSE","LOSS","LOT","LOVE","LOVELY","LOW","LUNCH","MACHINE","MAGAZINE","MAIN","MAINLY","MAINTAIN","MAJOR","MAJORITY","MAKE","MALE","MAN","MANAGE","MANAGEMENT","MANAGER","MANNER","MANY","MAP","MARK","MARKET","MARRIAGE","MARRIED","MARRY","MASS","MASTER","MATCH","MATERIAL","MATTER","MAY","MAYBE","ME","MEAL","MEAN","MEANING","MEANS","MEANWHILE","MEASURE","MECHANISM","MEDIA","MEDICAL","MEET","MEETING","MEMBER","MEMBERSHIP","MEMORY","MENTAL","MENTION","MERELY","MESSAGE","METAL","METHOD","MIDDLE","MIGHT","MILE","MILITARY","MILK","MIND","MINE","MINISTER","MINISTRY","MINUTE","MISS","MISTAKE","MODEL","MODERN","MODULE","MOMENT","MONEY","MONTH","MORE","MORNING","MOST","MOTHER","MOTION","MOTOR","MOUNTAIN","MOUTH","MOVE","MOVEMENT","MUCH","MURDER","MUSEUM","MUSIC","MUST","MY","MYSELF","NAME","NARROW","NATION","NATIONAL","NATURAL","NATURE","NEAR","NEARLY","NECESSARILY","NECESSARY","NECK","NEED","NEGOTIATION","NEIGHBOUR","NEITHER","NETWORK","NEVER","NEVERTHELESS","NEW","NEWS","NEWSPAPER","NEXT","NICE","NIGHT","NO","NOBODY","NOD","NOISE","NONE","NOR","NORMAL","NORMALLY","NORTH","NORTHERN","NOSE","NOT","NOTE","NOTHING","NOTICE","NOTION","NOW","NUCLEAR","NUMBER","NURSE","OBJECT","OBJECTIVE","OBSERVATION","OBSERVE","OBTAIN","OBVIOUS","OBVIOUSLY","OCCASION","OCCUR","ODD","OF","OFF","OFFENCE","OFFER","OFFICE","OFFICER","OFFICIAL","OFTEN","OIL","OKAY","OLD","ON","ONCE","ONE","ONLY","ONTO","OPEN","OPERATE","OPERATION","OPINION","OPPORTUNITY","OPPOSITION","OPTION","OR","ORDER","ORDINARY","ORGANISATION","ORGANISE","ORGANIZATION","ORIGIN","ORIGINAL","OTHER","OTHERWISE","OUGHT","OUR","OURSELVES","OUT","OUTCOME","OUTPUT","OUTSIDE","OVER","OVERALL","OWN","OWNER","PACKAGE","PAGE","PAIN","PAINT","PAINTING","PAIR","PANEL","PAPER","PARENT","PARK","PARLIAMENT","PART","PARTICULAR","PARTICULARLY","PARTLY","PARTNER","PARTY","PASS","PASSAGE","PAST","PATH","PATIENT","PATTERN","PAY","PAYMENT","PEACE","PENSION","PEOPLE","PER","PERCENT","PERFECT","PERFORM","PERFORMANCE","PERHAPS","PERIOD","PERMANENT","PERSON","PERSONAL","PERSUADE","PHASE","PHONE","PHOTOGRAPH","PHYSICAL","PICK","PICTURE","PIECE","PLACE","PLAN","PLANNING","PLANT","PLASTIC","PLATE","PLAY","PLAYER","PLEASE","PLEASURE","PLENTY","PLUS","POCKET","POINT","POLICE","POLICY","POLITICAL","POLITICS","POOL","POOR","POPULAR","POPULATION","POSITION","POSITIVE","POSSIBILITY","POSSIBLE","POSSIBLY","POST","POTENTIAL","POUND","POWER","POWERFUL","PRACTICAL","PRACTICE","PREFER","PREPARE","PRESENCE","PRESENT","PRESIDENT","PRESS","PRESSURE","PRETTY","PREVENT","PREVIOUS","PREVIOUSLY","PRICE","PRIMARY","PRIME","PRINCIPLE","PRIORITY","PRISON","PRISONER","PRIVATE","PROBABLY","PROBLEM","PROCEDURE","PROCESS","PRODUCE","PRODUCT","PRODUCTION","PROFESSIONAL","PROFIT","PROGRAM","PROGRAMME","PROGRESS","PROJECT","PROMISE","PROMOTE","PROPER","PROPERLY","PROPERTY","PROPORTION","PROPOSE","PROPOSAL","PROSPECT","PROTECT","PROTECTION","PROVE","PROVIDE","PROVIDED","PROVISION","PUB","PUBLIC","PUBLICATION","PUBLISH","PULL","PUPIL","PURPOSE","PUSH","PUT","QUALITY","QUARTER","QUESTION","QUICK","QUICKLY","QUIET","QUITE","RACE","RADIO","RAILWAY","RAIN","RAISE","RANGE","RAPIDLY","RARE","RATE","RATHER","REACH","REACTION","READ","READER","READING","READY","REAL","REALISE","REALITY","REALIZE","REALLY","REASON","REASONABLE","RECALL","RECEIVE","RECENT","RECENTLY","RECOGNISE","RECOGNITION","RECOGNIZE","RECOMMEND","RECORD","RECOVER","RED","REDUCE","REDUCTION","REFER","REFERENCE","REFLECT","REFORM","REFUSE","REGARD","REGION","REGIONAL","REGULAR","REGULATION","REJECT","RELATE","RELATION","RELATIONSHIP","RELATIVE","RELATIVELY","RELEASE","RELEVANT","RELIEF","RELIGION","RELIGIOUS","RELY","REMAIN","REMEMBER","REMIND","REMOVE","REPEAT","REPLACE","REPLY","REPORT","REPRESENT","REPRESENTATION","REPRESENTATIVE","REQUEST","REQUIRE","REQUIREMENT","RESEARCH","RESOURCE","RESPECT","RESPOND","RESPONSE","RESPONSIBILITY","RESPONSIBLE","REST","RESTAURANT","RESULT","RETAIN","RETURN","REVEAL","REVENUE","REVIEW","REVOLUTION","RICH","RIDE","RIGHT","RING","RISE","RISK","RIVER","ROAD","ROCK","ROLE","ROLL","ROOF","ROOM","ROUND","ROUTE","ROW","ROYAL","RULE","RUN","RURAL","SAFE","SAFETY","SALE","SAME","SAMPLE","SATISFY","SAVE","SAY","SCALE","SCENE","SCHEME","SCHOOL","SCIENCE","SCIENTIFIC","SCIENTIST","SCORE","SCREEN","SEA","SEARCH","SEASON","SEAT","SECOND","SECONDARY","SECRETARY","SECTION","SECTOR","SECURE","SECURITY","SEE","SEEK","SEEM","SELECT","SELECTION","SELL","SEND","SENIOR","SENSE","SENTENCE","SEPARATE","SEQUENCE","SERIES","SERIOUS","SERIOUSLY","SERVANT","SERVE","SERVICE","SESSION","SET","SETTLE","SETTLEMENT","SEVERAL","SEVERE","SEX","SEXUAL","SHAKE","SHALL","SHAPE","SHARE","SHE","SHEET","SHIP","SHOE","SHOOT","SHOP","SHORT","SHOT","SHOULD","SHOULDER","SHOUT","SHOW","SHUT","SIDE","SIGHT","SIGN","SIGNAL","SIGNIFICANCE","SIGNIFICANT","SILENCE","SIMILAR","SIMPLE","SIMPLY","SINCE","SING","SINGLE","SIR","SISTER","SIT","SITE","SITUATION","SIZE","SKILL","SKIN","SKY","SLEEP","SLIGHTLY","SLIP","SLOW","SLOWLY","SMALL","SMILE","SO","SOCIAL","SOCIETY","SOFT","SOFTWARE","SOIL","SOLDIER","SOLICITOR","SOLUTION","SOME","SOMEBODY","SOMEONE","SOMETHING","SOMETIMES","SOMEWHAT","SOMEWHERE","SON","SONG","SOON","SORRY","SORT","SOUND","SOURCE","SOUTH","SOUTHERN","SPACE","SPEAK","SPEAKER","SPECIAL","SPECIES","SPECIFIC","SPEECH","SPEED","SPEND","SPIRIT","SPORT","SPOT","SPREAD","SPRING","STAFF","STAGE","STAND","STANDARD","STAR","START","STATE","STATEMENT","STATION","STATUS","STAY","STEAL","STEP","STICK","STILL","STOCK","STONE","STOP","STORE","STORY","STRAIGHT","STRANGE","STRATEGY","STREET","STRENGTH","STRIKE","STRONG","STRONGLY","STRUCTURE","STUDENT","STUDIO","STUDY","STUFF","STYLE","SUBJECT","SUBSTANTIAL","SUCCEED","SUCCESS","SUCCESSFUL","SUCH","SUDDENLY","SUFFER","SUFFICIENT","SUGGEST","SUGGESTION","SUITABLE","SUM","SUMMER","SUN","SUPPLY","SUPPORT","SUPPOSE","SURE","SURELY","SURFACE","SURPRISE","SURROUND","SURVEY","SURVIVE","SWITCH","SYSTEM","TABLE","TAKE","TALK","TALL","TAPE","TARGET","TASK","TAX","TEA","TEACH","TEACHER","TEACHING","TEAM","TEAR","TECHNICAL","TECHNIQUE","TECHNOLOGY","TELEPHONE","TELEVISION","TELL","TEMPERATURE","TEND","TERM","TERMS","TERRIBLE","TEST","TEXT","THAN","THANK","THANKS","THAT","THE","THEATRE","THEIR","THEM","THEME","THEMSELVES","THEN","THEORY","THERE","THEREFORE","THESE","THEY","THIN","THING","THINK","THIS","THOSE","THOUGH","THOUGHT","THREAT","THREATEN","THROUGH","THROUGHOUT","THROW","THUS","TICKET","TIME","TINY","TITLE","TO","TODAY","TOGETHER","TOMORROW","TONE","TONIGHT","TOO","TOOL","TOOTH","TOP","TOTAL","TOTALLY","TOUCH","TOUR","TOWARDS","TOWN","TRACK","TRADE","TRADITION","TRADITIONAL","TRAFFIC","TRAIN","TRAINING","TRANSFER","TRANSPORT","TRAVEL","TREAT","TREATMENT","TREATY","TREE","TREND","TRIAL","TRIP","TROOP","TROUBLE","TRUE","TRUST","TRUTH","TRY","TURN","TWICE","TYPE","TYPICAL","UNABLE","UNDER","UNDERSTAND","UNDERSTANDING","UNDERTAKE","UNEMPLOYMENT","UNFORTUNATELY","UNION","UNIT","UNITED","UNIVERSITY","UNLESS","UNLIKELY","UNTIL","UP","UPON","UPPER","URBAN","US","USE","USED","USEFUL","USER","USUAL","USUALLY","VALUE","VARIATION","VARIETY","VARIOUS","VARY","VAST","VEHICLE","VERSION","VERY","VIA","VICTIM","VICTORY","VIDEO","VIEW","VILLAGE","VIOLENCE","VISION","VISIT","VISITOR","VITAL","VOICE","VOLUME","VOTE","WAGE","WAIT","WALK","WALL","WANT","WAR","WARM","WARN","WASH","WATCH","WATER","WAVE","WAY","WE","WEAK","WEAPON","WEAR","WEATHER","WEEK","WEEKEND","WEIGHT","WELCOME","WELFARE","WELL","WEST","WESTERN","WHAT","WHATEVER","WHEN","WHERE","WHEREAS","WHETHER","WHICH","WHILE","WHILST","WHITE","WHO","WHOLE","WHOM","WHOSE","WHY","WIDE","WIDELY","WIFE","WILD","WILL","WIN","WIND","WINDOW","WINE","WING","WINNER","WINTER","WISH","WITH","WITHDRAW","WITHIN","WITHOUT","WOMAN","WONDER","WONDERFUL","WOOD","WORD","WORK","WORKER","WORKING","WORKS","WORLD","WORRY","WORTH","WOULD","WRITE","WRITER","WRITING","WRONG","YARD","YEAH","YEAR","YES","YESTERDAY","YET","YOU","YOUNG","YOUR","YOURSELF","YOUTH"]

def isTriangleWord(word):
    ts = {triangleNumber(n) for n in range(1,50)}
    s = sum([ord(c)-64 for c in word])
    return s in ts

def euler042():
    return [isTriangleWord(word) for word in fourtyTwoText].count(True)
        
def euler050(below = 1000000):
    '''finished at 2011-07-29-1938'''
    primes = primeSieve2(below)
    i = 0
    accum = 0
    primeSums = []
    while(accum<below): # get all the sums of primes from 2 to below
        accum+=primes[i]
        primeSums.append(accum)
        i+=1
    #print( primes)
    #print (primeSums)
    diff = 1 #difference between two primes that is the consecutive
    bigPrime = 2 # biggest prime encountered so far that is the sequence of consecutive prime, aka first prime (2) by itself
    for lo,p in enumerate(primeSums):
        for hi in range(lo+diff,len(primeSums)):
            n = primeSums[hi] - primeSums[lo]
            if hi-lo > diff and isPrime(n):
                diff = hi-lo
                bigPrime = n
    return bigPrime

def euler039():
    '''pythagorean triples'''
    triples = []
    for i in range(1,1000):
        for j in range(1, 1000):
            for k in range(1,1000):
                if i<j and j<k and i*i+j*j == k*k:
                    triples.append((i,j,k))
    # with the triples, calculate the perimeter length of each triangle
    # use a defaultDict to collapse everything with the same perimeter into a sum
    return triples
                
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("problem")
    args = parser.parse_args()
    solution = "euler"+args.problem
    l.warning("running " + solution)
    if solution in globals():
        func = globals()[solution]
        if inspect.isfunction(func):
            print(func())
    else:
        return -1
    return 0

if __name__ == '__main__':
    sys.exit(main())

