# Python3
input_ = int(input())
if input_<=1:
    print(input_)  
    exit()

def func(input_):
    a, b = 0, 1
    for _ in range(input_ - 1):
        c = a + b
        b, a = c, b
    print(c)

func(input_)
