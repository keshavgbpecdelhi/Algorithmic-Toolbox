#greedy-3.4
#9Nov2020
n = int(input())
x = [int(a) for a in input().split()] #x is the profit per click of the a-th ad
y = [int(a) for a in input().split()] #y is the average number of clicks per day of the a-th slot
x.sort()
y.sort()
max_earning = sum([x[a]*y[a] for a in range(n)])
print(max_earning)