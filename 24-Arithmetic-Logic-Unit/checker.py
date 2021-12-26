import sys
f = False # for clarity
A        = [   12,   15,   11,  -14,   12,  -10,   11,   13,   -7,   10,   -2,   -1,   -4,  -12]
B        = [    4,   11,    7,    2,   11,   13,    9,   12,    6,    2,   11,   12,    3,   13]
divisions= [    f,    f,    f, True,    f, True,    f,    f, True,    f, True, True, True, True]
def step(input, z, A, B):
    if len(z) > 0:
        x = z[len(z) - 1]
    else:
        x = 0
    if A < 0:
        # print('pop')
        z.pop()
    if x+A != input:
        print(f'append x{x}+A{A} != {input}')
        z.append(input + B)
    return z

modelNumber = sys.argv[1]
i = 0
z = []
for i in range(len(modelNumber)):
    z = step(int(modelNumber[i]), z, A[i], B[i])
print(z)
