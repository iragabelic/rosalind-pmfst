a = input("Enter: ")
def complement(a):
    a = a.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T').replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')
    return a[::-1]

print(complement(a))
##TEMP se stvara da bi drzala privremenu vrijednost
