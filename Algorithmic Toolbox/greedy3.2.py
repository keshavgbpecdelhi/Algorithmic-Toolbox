#greedy-3.2
#9Nov2020
no, W = [int(a) for a in input().split()]
if W == 0:
    print(0)
    exit()

loot = 0    
list_ = []

for _ in range(no):
    v, w = [int(a) for a in input().split()]
    if v == 0:
        continue
    list_.append((v, w))

list_.sort(key = lambda x: x[0]/x[1], reverse = True)


for v,w in list_:
    if W==0:
        print(loot)
        exit()
    amount = min(w, W)
    loot += amount*v/w
    W -= amount

print(loot)

