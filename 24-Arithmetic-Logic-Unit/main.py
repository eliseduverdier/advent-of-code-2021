import sys
f = False # for clarity

'''
                             8/9---1/2
                                       1>8----2>9
                                                          1>4--6>9
                                                                     all=
                                                     ??-------------------------??
                       1----------------------------------------------------------------9 nope (2-8/1-9)
                ??----------------------------------------------------------------------------??
largest:  __9289_4999___
smallest: __8112_1611___
'''
A        = [   12,   15,   11,  -14,   12,  -10,   11,   13,   -7,   10,   -2,   -1,   -4,  -12]
B        = [    4,   11,    7,    2,   11,   13,    9,   12,    6,    2,   11,   12,    3,   13]
divisions= [    f,    f,    f, True,    f, True,    f,    f, True,    f, True, True, True, True]
#                               -7            1                 5           0    10     8    -9
'''
they should cancel each other out like a stack. the ones appended corresponding to the ones popped

example to keep 99811211691  ->  [13, 20, 10, 11]

 when POP, should not APPEND !!!
 => when POP, A+lastInput+lastB   should equals INPUT
 (so oly when negative numbers)
                                     -> xxx
 -14 + 7  (-7) + last input == input -> xx81
 -10 + 11 ( 1) + last input == input -> xx8198
 -7+12    ( 5)                       -> xx8198
 -2+2     ( 0)                       -> xx8198x?
 -1+11    (10)                       -> xx8198x55
 -4+12    ( 8)                       -> xx8198x553
 -12+3    (-9)                       -> xx819855539


'''

# keep 9992121160  ->  [13, 20, 10, 2]


# a[i+1] + b[i] = 12 19, 22, -7, 14,  1, 24, 22,  5, 16,  0, 10, 8, -9
# a[i] + b[i+1] = 4, 23, 22, 13, -3, 25, -1, 23, 19, -5, 21, 10, 2, 9
#                            ---     ---         ---
def step(input, z, A, B):
    if len(z) > 0:
        x = z[len(z) - 1]
    else:
        x = 0
    if A < 0:
        z.pop()
    x += A        # >>>> x = A + last z(=lastInput+B)    should equals input
    # we need A + lastInput+B == input
    if x != input:
        z.append(input + B)
    return z

def testIsValid(modelNumber):
    i = 0
    z = []
    for i in range(len(modelNumber)):
        z = step(int(modelNumber[i]), z, A[i], B[i])
    return z

# the wiggle room left
for a in range(9,0,-1): # 1
    for b in range(9,0,-1): # 2
        for c in range(9,0,-1): # 3
            for d in range(9,0,-1): # 3
                for e in range(9,0,-1): # 3
                    for f in range(9,0,-1): # 3
                        modelNumber = str(a)+str(b)+'8112'+str(c)+'1611'+str(d)+str(e)+str(f) # the smallest
                        # modelNumber = str(a)+str(b)+'9289'+str(c)+'4999'+str(d)+str(e)+str(f) # the largest
                        z = testIsValid(modelNumber)
                        if len(z) == 0:
                            print(modelNumber,' -> ',z)
# 92928914999991  ->  []
# 91928914999981  ->  []