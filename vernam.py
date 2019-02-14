def text_to_bin(text):
    binary=[]
    for i in text:
        d=ord(i)
        b=''
        while d!=0:
            m=str(d%2)
            b+=m
            d=d//2
        
        binary.append(b[::-1])

    return binary

def xor(bin1,bin2):
    res=[]
    for m,n in zip(bin1,bin2):
        ans=''
        for i,j in zip(m,n):
            if i==j:
                ans+='0'
            else:
                ans+='1'
        res.append(ans)
    return res

def bin_to_dec(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal     
        

def encrypt(key,plain):
    b_key=text_to_bin(key.lower())
    b_plain=text_to_bin(plain.lower())

    print("Binary key: ",''.join(b_key))
    print("Binary plain text: ",''.join(b_plain))
    
    b_xor=xor(b_key,b_plain)
    print("XOR result: ",''.join(b_xor))
    
    text =[]
    for i in b_xor:
        t=bin_to_dec(int(i))
        text.append(t)

    return text



key=input("Enter key: ")
plain=input("Enter plain text: ")
enc=encrypt(key,plain)
print("Encrypted text: ",''.join([str(i) for i in enc]))
    

    
        
