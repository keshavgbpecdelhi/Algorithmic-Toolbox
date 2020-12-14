#gcd
a, b = [int(i) for i in input().split()]

def gcd_(a, b):
    if b == 0:
        print(a) #printing other if anyone of them is zero
        exit() 
    c = a % b  #taking modulous 
    gcd_(b, c) #recursion calling the same function to perform the same task with smaller numbers.
	
#This perticual if else is get the modulous accordingly so as no zero % come due to mismatch.
if a>b:
    gcd_(a, b)
else:
    gcd_(b, a)
