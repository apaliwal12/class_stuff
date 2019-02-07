def createTable():
    mat = []
    lst = []

    for i in range(65, 91):
        lst.append(chr(i))

    for i in range(0, 26):
        mat.append([])
        for j in range(0,26):
            mat[i].append(lst[(j+i)%26])
    
    for i in range(0, 26):
        print(' '.join(mat[i]))

    return mat
    

def vignere(key,text):
    mat=createTable()
    com=zip(list(key),list(text))
    ciph_text=''
    for i,j in com:
        ciph_text=ciph_text+mat[ord(i)-97][ord(j)-97]
    return ciph_text

key=input("Enter key: ")
ptext=input("Enter plain text: ")
print("Cipher text:",vignere(key,ptext))
        

