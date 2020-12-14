#  Number of Inversions
# Problem Introduction
# An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such
# that 𝑎𝑖 > 𝑎𝑗 . The number of inversions of a sequence in some sense measures how
# close the sequence is to being sorted. For example, a sorted (in non-descending
# order) sequence contains no inversions at all, while in a sequence sorted in 
#descending order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2
# inversions).
# 6 1 5 2 3
# Problem Description
# Task. The goal in this problem is to count the number of inversions of a given sequence.
# Input Format. The first line contains an integer 𝑛, the next one contains a sequence of integers
# 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
# Constraints. 1 ≤ 𝑛 ≤ 105
# , 1 ≤ 𝑎𝑖 ≤ 109
# for all 0 ≤ 𝑖 < 𝑛.
# Output Format. Output the number of inversions in the sequence.
# Sample 1.
# Input:
# 5
# 2 3 9 2 9
# Output:
# 2
# The two inversions here are (1, 3) (𝑎1 = 3 > 2 = 𝑎3) and (2, 3) (𝑎2 = 9 > 2 = 𝑎3).
# What To Do
# This problem can be solved by modifying the merge sort algorithm. For this, we change both the Merge and
# MergeSort procedures as follows:
# ∙ Merge(𝐵, 𝐶) returns the resulting sorted array and the number of pairs (𝑏, 𝑐) such that 𝑏 ∈ 𝐵, 𝑐 ∈ 𝐶,
# and 𝑏 > 𝑐;
# ∙ MergeSort(𝐴) returns a sorted array 𝐴 and the number of inversions in 𝐴.

#-----------solution---------------
def merge(left, right):
    i, j, count_inv = 0, 0, 0
    latest = list()
    while i < len(left) and j< len(right):
        if left[i] <= right[j]:
            latest.append(left[i])
            i += 1
        else:
            latest.append(right[j])
            count_inv += len(left) - i
            j += 1

    latest += left[i:]
    latest += right[j:]
        
    return latest, count_inv

def merge_sort(arr):
    global count_total
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    count_total += temp

    return sorted_arr

count_total = 0
n = int(input())
seq = [int(i) for i in input().split()]
merge_sort(seq)
print(count_total)


