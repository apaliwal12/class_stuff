alpha=['a','b','c','d','e','f','g','h',
       'i','j','k','l','m','n','o',
       'p','r','s','t','u','v',
       'w','x','y','z']

def kmatrix(k):
    if ' ' in k:
        l=k.split()
        k=''.join(l)
    mod_k=''
    for i in k:
        if i not in mod_k:
            mod_k=mod_k+i

    for i in alpha:
        if i not in mod_k:
            mod_k+=i  

    
    mat=[[],[],[],[],[]]

    m=0
    for i in range(5):
        for j in range(5):
            mat[i].append(mod_k[m])
            m+=1
            

##    for first in mat:
##        for second in first:
##            print(second, end=' ')
##        print()


    return mat

def ptext(text):
    text=text.split()
    text=''.join(text)

    for i in range(1,len(text)):
        if text[i]==text[i-1]:
            text=text[0:i]+'x'+text[i:]
        
    if len(text)%2!=0:
        text=text+'z'
    return text
    

def encrypt(keymat,matrix,a,b):
    col1, col2, row1, row2 = 0,0,0,0
    col1 = int(matrix.index(a)%5)
    col2 =  int(matrix.index(b)%5)
    temp = ""

    row1 = int(matrix.index(a)/5)
    row2 =  int(matrix.index(b)/5)

    if (col1==col2) and (row1!=row2):           #Same Column
        temp = temp + keymat[(row1+1)%5][col1] + keymat[(row2+1)%5][col1]
    elif (col1!=col2) and (row1==row2):         #Same Row
        temp = temp + keymat[row1][(col1+1)%5] + keymat[row1][(col2+1)%5]
    elif (col1!=col2) and (row1!=row2):         #Rectangle
        temp = temp + keymat[row1][col2] + keymat[row2][col1] 
    return temp
    
def playfair(st,k):
    kmat=kmatrix(k.lower())
    print("\nKey matrix:")
    for row in kmat:
        print(' '.join(row))
    pt=ptext(st.lower())
    mlst=[]
    final=''
    for row in kmat:
        mlst.extend(row)

    for i in range(1,len(pt),2):
        final=final+encrypt(kmat,mlst, pt[i-1],pt[i])
            
    return final

key=input("Enter key: ")
ptext1=input("Enter plain text: ")
print("\nEncrypted text: ",playfair(ptext1,key))
