def kSortingReversal(P,k):
    j=k
    while P[j]!=k+1 and P[j]!=-(k+1):
        j+=1
        
    P[k:(j+1)]=list(map(funkcija,P[k:(j+1)][::-1]))
    return P
        
    
def funkcija(x):
    return -x
    

def GreedySorting(P):
    P = P.strip().replace("(","").replace(")","").split()
    niz = []
    for p in P:
        niz.append(int(p))
    for k in range(0,len(niz)):
        if niz[k]!=k+1:
            niz=kSortingReversal(niz,k)
            print("("+" ".join(["+"+str(el) if el>0 else str(el) for el in niz])+")")
            if niz[k]==-(k+1):
                niz=kSortingReversal(niz,k)
                print("("+" ".join(["+"+str(el) if el>0 else str(el) for el in niz])+")")

GreedySorting("""(+139 +102 -126 -58 -89 +53 -66 -69 -99 -112 -13 +41 +37 -96 +16 +98 +142 -141 -35 -50 -118 +36 +11 +92 +65 -136 -28 -94 +54 +9 -26 +84 +138 +39 -8 +140 +83 -117 +113 +21 -55 -104 +129 -15 +48 +2 +49 +52 -101 +22 +143 -7 +61 +29 -121 -130 -88 +67 +91 -24 -34 -128 -18 +5 +81 +107 -1 -19 +45 +109 -85 -40 +122 -95 -108 +68 +73 +100 +25 +78 -115 +111 +31 +63 +76 +14 +125 -51 -23 -80 -4 -44 -132 -46 -42 -127 -56 -75 -133 -38 +30 +33 -64 +3 -43 -123 +105 -47 -93 +57 +32 +17 +103 -62 +114 +60 +137 +74 +79 +12 +82 -135 -134 -71 -116 -86 +131 -124 -110 -70 -77 -27 +20 +72 +120 -59 +90 -6 -10 +119 -97 +87 -106)""")
