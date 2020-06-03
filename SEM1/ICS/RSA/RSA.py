choice = 999


def gcdExtended(a, b, x, y): 
	# Base Case 
	if a == 0 : 
		x = 0
		y = 1
		return b 
		
	x1 = 1
	y1 = 1 # To store results of recursive call 
	gcd = gcdExtended(b%a, a, x1, y1) 

	# Update x and y using results of recursive 
	# call 
	x = y1 - (b/a) * x1 
	y = x1 

	return gcd 

def factor(n,e):
    list = []
    for i in range(1, n + 1):
       if n % i == 0:
           if e == i:
               return False
       else:
            return True

p = int(input("Enter p : "))
q = int(input("Enter q : "))
n = p*q
phi = (p-1)*(q-1)

while True:
    e = int(input("Enter e : "))
    if (e < phi and e > 1) and factor(n,e):
        break

x = 1
y = 1
d = gcdExtended(e, phi, x, y) 
print("gcd(", e , "," , phi, ") = ", d) 
    
print(" e = ",e,"\n d = ",d,"\n phi = ",phi,"\n n = ",n)
#CT = 129
while choice != 0:
        choice = int(input('''

        $$ M E N U $$
    1) Encryption
    2) Decryption
    0) Exit

    Enter Your Choice?     '''))
        
        if choice != 0:
                with open("file.txt", 'r') as f:
                        msg = f.read()
                        f.close()
        if choice == 1:
                print('PT = ',msg)
                CT = (int(msg)**e) % n
                print("Encypted Data : ",CT)
                
        elif choice == 2:
                PT_Enc = (CT**d) % n
                print("Decrypted Data : ",PT_Enc)

        elif choice == 0:
                print("Thank You !!!!")
        else:
                print("INVALID CHOICE!!")


# Python program to demonstrate working of extended 
# Euclidean Algorithm 


x = 1
y = 1
a = 35
b = 15

                
