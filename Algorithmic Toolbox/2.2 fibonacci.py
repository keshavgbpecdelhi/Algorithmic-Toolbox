#last_digit_of_fibonacci = ldof

#input_ = int(input())
#if input_<=1:
    #print(input_)
#def ldof(input_):
    #x, y = 0, 1
    #for i in range(input_-1):
        #z = x + y
        #z = z % 10
        #y, z = z, y
    #print(z)
#ldof(input_)

def ldof(n):
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b) % 10
        print(b)

n = int(input())
ldof(n)