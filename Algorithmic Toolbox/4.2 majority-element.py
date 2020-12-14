# Majority Element 
n = int(input())
sequence = [int(i) for i in input().split()] #input sequence

def func(sequence, l, r):
    if l+1==r:
        return sequence[l]
    elif l+2==r:
        return sequence[l]
    m = (l+r)//2
    _left = func(sequence, l, m)
    _right = func(sequence, m, r)

    c1, c2 = 0, 0
    for i in sequence[l:r]:
        if i == _left:
            c1+=1
        elif i == _right:
            c2+=1
    if c1>(r-l)//2 and _left != -1:
        return _left
    elif c2>(r-l)//2 and _right != -1:
        return _right
    else: 
        return -1

print(int(func(sequence, 0, n) != -1))
