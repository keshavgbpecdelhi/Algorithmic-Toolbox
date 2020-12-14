#6 Last Digit of the Sum of Fibonacci Numbers

n = int(input()) #let the input be n

#We r gonna exit if our input got less value then 1 
if n<=1: 
    print(n)  
    exit()


l = (n+2)%60 

#after doing the above maths if l turned out to be 1 or 0 then when gonna exit.
if l==1:
    print(0)
    exit()
	
elif l==0:
    print(9)
    exit()

#if not then this function will do the work.	
def func(n):
    a,b = 0, 1
    for _ in range(2,l+1):
        c = a+b
        c = c%10
        b, a = c, b
    if c!=0:
        print(c-1)
    else:
        print(9)
func(l)
