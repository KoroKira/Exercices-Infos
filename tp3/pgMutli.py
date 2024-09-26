from pgSomme import somme

def multi(nbr1, nbr2):
    return nbr1 * nbr2

# test
if __name__ =="__main__":
    m=multi(3,2.2)
    print(m) # 6.6
    S=somme(3,2.2)
    print(S)