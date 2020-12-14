#greedy-3.1
#9Nov2020
no = int(input())
cnt = 0
for a in [1, 5, 10]:
    if no >= a:
        cnt+= no//a
        no%= a
        if no == 0:
            print(cnt)
            exit()

