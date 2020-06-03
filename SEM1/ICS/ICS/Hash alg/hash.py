from hashlib import sha1,md5

print(''' $$ M E N U $$
1) Use openSSL toolkit of cryptographic functions and expertiment with different implementations of Hash functions i.e MD5, SHA-1 
2) One of the desirable properties of cryptographic Hash function is the Avalanche Effect i.e change in a single bit of input would result in drastic change in Hash value. Demonstarte the Avalanche property of MD5 and SHA-2 by creating Hash of two different files which are differeing in single bit.
3)Write a program/script that will find collisions in Hash functions. For this purpose you can take 4 bytes of input and 3 bytes of Hash value. Compute the average time required to find the collisions in MD5.
''')
choice = int(input('Choice ?  '))

if choice == 1:
    f = open("test1.txt","r")
    data = f.read()
    print('Actual data        : ',data)
    sha = sha1(data.encode())
    md = md5(data.encode())
    print('MD5 Hashed Value   : ',md.hexdigest())
    print('SHA-1 Hashed Value : ',sha.hexdigest())

elif choice == 2:
    f1 = open("test1.txt","r")
    dataa = f1.read()
    shaa = sha1(dataa.encode())
    mda = md5(dataa.encode())
    f2 = open("test2.txt","r")
    datab = f2.read()
    shab = sha1(datab.encode())
    mdb = md5(datab.encode())
    print('Actual data(test1.txt)        : ',dataa)
    print('Actual data(test2.txt)        : ',datab)
    print('MD5 Hashed Value(test1.txt)   : ',mda.hexdigest())
    print('MD5 Hashed Value(test2.txt)   : ',mdb.hexdigest())
    
    print('SHA-1 Hashed Value(test1.txt) : ',shaa.hexdigest())
    print('SHA-1 Hashed Value(test2.txt) : ',shab.hexdigest())
else:
    print('Third Choice Working')
