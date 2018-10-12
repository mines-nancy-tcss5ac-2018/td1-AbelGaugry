def test_palindrome(n):
    l=str(n) 
    i=0 
    j=len(l)-1 
    bool=True 
    while (i<j and bool):
        if l[i] != l[j]:
            bool=False
            i+=1 
            j-=1 
    return bool 




#print(test_palindrome(15851)) 


def reverse(n):
     l1=str(n) 
     l2="" 
     for i in range(len(l1)-1,-1,-1):
         l2+=l1[i] 
    return int(l2) 


# print (reverse(1984)) 


def test_lychrel(n,num_iteration):
    N=n+reverse(n) 
    #print(N) 
    if test_palindrome(N):
        return False 
    elif num_iteration>50:
        return True
    else:
        return test_lychrel(N,num_iteration+1) 



#print(test_lychrel(349,1)) 



def compte_lych(n):
    somme=0 
    for i in range(n):
        if test_lychrel(i,1):
            somme+=1 
    return somme 


# print(compte_lych(10000))