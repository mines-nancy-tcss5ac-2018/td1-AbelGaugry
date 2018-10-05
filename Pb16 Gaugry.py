def solve(n):
    r=0
    a=2**n
    while a!=0:
        r+=n%10
        a=a//10
    return(r)