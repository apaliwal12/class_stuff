#ceaser cipher

alpha=['a','b','c','d','e','f','g','h',
       'i','j','k','l','m','n','o',
       'p','q','r','s','t','u','v',
       'w','x','y','z']

def encrypt(st,k):
    est=''
    for i in st:
        est+=alpha[(alpha.index(i)+k)%26]

    return est

def decrypt(st,k):
    dst=''
    for i in st:
        dst+=alpha[(alpha.index(i)-k)%26]

    return dst


def cipher(st,k):
    ch=int(input("1.Encrypt\n2.Decrypt\n"))

    if ch==1:
        return encrypt(st,k)
    elif ch==2:
        return decrypt(st,k)
    else:
        print("Wrong Choice!!")
        cipher(st,k)

while 1:
    string,key=input("Enter string followed by key: ").split()
    key=int(key)

    print("Answer is: ",cipher(string.lower(),key))
    ch=input("Continue? [Y/N]")
    if ch.lower()=='y':
        continue
    else:
        break





    
