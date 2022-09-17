def CountingPeptides(d,mase):
    broj_peptida={}
    for i in range(57):
        broj_peptida[i]=0

    for i in range(57,d+1):
        broj_peptida[i]=mase.count(i)
        for m in mase:
            if(i>=m):
                broj_peptida[i]+=broj_peptida[i-m]


    return broj_peptida[i]

mase=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128,
      129, 131, 137, 147, 156, 163, 186]
print(CountingPeptides(1024,mase))#1308 je dana masa iz dataseta
