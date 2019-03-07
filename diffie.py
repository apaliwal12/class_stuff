import sys
sys.setrecursionlimit(10000)

def power(a,b,mod):
    if b==1:
        return a
    t=power(a,b/2,mod)
    if b%2==0:
        return (t*t)%mod
    else:
        return (((t*t)%mod)*a)%mod


def calculateKey(a,x,n):
    return power(a,x,n)

def main():
    # both the persons will be agreed upon the common n and g
    n,g=map(int,input("Enter the value of n and g: ").split())

    # first person will choose the x
    x=int(input("Enter the value of x for the first person: "))
    a=power(g,x,n)

    #second person will choose the y
    y=int(input("Enter the value of y for the second person: "))
    b=power(g,y,n)

    print("key for the first person is:",power(b,x,n))
    print("key for the second person is",power(a,y,n))

main()
