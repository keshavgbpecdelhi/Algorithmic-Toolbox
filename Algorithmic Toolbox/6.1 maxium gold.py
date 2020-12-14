# Uses python3
# Maximum Gold Problem
# Using ow for optimal_weight
import sys


def ow(W, w):
    w = [0] + w
    items = len(w)
    capacity = W + 1
    w_ = [[0 for _ in range(items)] for _ in range(capacity)]

    for j in range(1, items):
        for i in range(1, capacity):
            prev = w_[i][j - 1]
            cur = w[j] + w_[W - w[j]][j - 1]
            if cur > i:
                w_[i][j] = prev
            else:
                w_[i][j] = max(prev, cur)

    return w_[-1][-1]


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(ow(W, w))
