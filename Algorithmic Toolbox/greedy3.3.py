#greedy-3.3
#9NOV2020

def refill(dist ,max_run, gstops):
    s = lsv = index = 0
    gstops.append(dist)
    while index < len(gstops):
        if gstops[index] - lsv <= max_run:
            index += 1
            continue
        elif gstops[index] - gstops[index-1] > max_run or index == 0:
            return -1
        else:
            lsv = gstops[index-1]
            s += 1
    return s

if __name__ == '__main__':

    distance_ = int(input())
    maximumRun = int(input())
    _ = int(input())
    checkpoint = list(map(int,input().split()))
    print(refill(distance_, maximumRun, checkpoint))