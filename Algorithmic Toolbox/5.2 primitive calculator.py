# --------------------Primitive Calculator---------------------------------
# Problem Introduction
# You are given a primitive calculator that can perform the following three operations with
# the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a
# positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛
# starting from the number 1.
# Problem Description
# Task. Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛
# starting from the number 1.
# Input Format. The input consists of a single integer 1 ≤ 𝑛 ≤ 106
# .
# Output Format. In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1.
# In the second line output a sequence of intermediate numbers. That is, the second line should contain
# positive integers 𝑎0, 𝑎2, . . . , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎𝑖+1 is equal to
# either 𝑎𝑖 + 1, 2𝑎𝑖
# , or 3𝑎𝑖
# . If there are many such sequences, output any one of them.
# Sample 1.
# Input:
# 1
# Output:
# 0
# 1
# Sample 2.
# Input:
# 5
# Output:
# 3
# 1 2 4 5
# Here, we first multiply 1 by 2 two times and then add 1. Another possibility is to first multiply by 3
# and then add 1 two times. Hence “1 3 4 5” is also a valid output in this case.
# Sample 3.
# Input:
# 96234
# Output:
# 14
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
# Again, another valid output in this case is “1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117
# 96234”.

# ------------Solution in python3 --------------------------

import math

n = int(input())
operator = [0, 0] + [math.inf]*(n-1)
for i in range(2, n+1):
    let1, let2, let3 = [math.inf]*3
    let1 = operator[i-1] + 1 
    if i%2 == 0: let2 = operator[i//2] + 1
    if i%3 == 0: let3 = operator[i//3] + 1
    min_ops = min(let1, let2, let3)
    operator[i] = min_ops
print(operator[n])
nums = [n]
while n!=1:
    if n%3 ==0 and operator[n]-1 == operator[n//3]:
        nums += [n//3]
        n = n//3
    elif n%2 ==0 and operator[n]-1 == operator[n//2]:
        nums += [n//2]
        n = n//2
    else:
        nums += [n-1]
        n = n - 1
print(' '.join([str(i) for i in nums][::-1]))