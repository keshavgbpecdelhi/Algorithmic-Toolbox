#binary search
# python solution
seq = [int(i) for i in input().split()] # taking input seq
search_seq = [int(i) for i in input().split()] # taking search seq
n = seq[0] #n is first seq element
seq = seq[1:] #rest is the seq

def bs_func(seq, i, r):
    l = 0
    while l<=r: 
        m = (l+r)//2
        if i > seq[m]:
            l = m + 1
        elif i < seq[m]:
            r = m - 1
        else:
            return m
    return -1

solution = list()
for i in search_seq[1:]:
    answer = bs_func(seq, i, n-1) #CALLING OF FUNC
    solution.append(answer)
print(' '.join([str(i) for i in solution]))

