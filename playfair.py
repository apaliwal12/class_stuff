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
    

def encrypt(mat,a,b):
    if mat.index(a)%5!=mat.index(b)%5 and mat.index(a)//5!=mat.index(b)//5:
        pass
    
    
def playfair(st,k):
    mat=kmatrix(k.lower())
    pt=ptext(st.lower())
    mlst=[]
    for row in mat:
        mlst.extend(row)

    for i in range(1,len(pt),2):
        encrypt(mlst, pt[i-1],pt[i])
            
    print(mlst)

print(playfair("hidethegold",'helloworld'))
                    
                

    
