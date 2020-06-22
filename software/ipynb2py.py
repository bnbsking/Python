import sys, os

with open(sys.argv[1], 'r+') as f:
    T, i, L = f.readlines(), 0, []
    while i<len(T):
        if T[i][:14] == "   \"source\": [" and T[i][-2]!=']':
            i+=1
            while T[i][:4] != '   ]' and T[i][:3] != ' ],':
                L.append(T[i])
                i+=1
        i+=1

for i in range(len(L)):
    l, r = 0, len(L[i])-1
    while L[i][l]!='\"':
        l+=1
    while L[i][r]!='\"':
        r-=1
    text = L[i][l+1:r]
    if text[-2:]=='\\n':
        text = text[:-2]
    
    new = ''
    for j in range(len(text)):
        if text[j]=='\\':
            try:
                if text[j+1]!='n':
                    continue
            except:
                pass
        new += text[j]
    L[i] = new
    
with open(sys.argv[2], "w+") as f:
    for i in range(len(L)):
        f.write(L[i]+"\n")

print("convert success !")
os.system("pause")
