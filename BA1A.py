inp = input("Enter string: ")
leng = int(input("Enter length: "))
kmers = []
pomocna = []
dic = {}
counter = 0
for i in range(len(inp)-2):
    kmers.append(inp[i:i+leng])
for j in range(len(kmers)):
    for k in range(j+1):
        if(kmers[j] == kmers[k]):
            counter += 1
            dic.update({str(kmers[j]): counter})
    counter = 0
for l in range(len(dic)):
    max_key = max(dic, key=dic.get)
    if(dic[l].value == max_key.value): ###max_key greska, mora bit value a ne key
        pomocna.append(dic[l].key)
        
    
print(pomocna)
