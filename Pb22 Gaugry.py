def alphabet(lettre):
    s=0
    alph=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    for i in range(len(alph)):
        if lettre == alph[i]:
            s=i+1
    return s

fichier = open('p022_names.txt', 'r')