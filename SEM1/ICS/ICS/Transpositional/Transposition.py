import math
choice = 999
print("\nNOTE : Enter key index starting from 0")
lst = []
key = input("\nEnter the Key  : ")

for i in range(len(key)):
	lst.append([])

def enc(msg, key):
	for i in range(0,len(msg),len(key)):
		for j in range(len(key)):
			if i+j < len(msg):
				lst[int(key[j])].append(msg[i+j])


def dec(enc, key):
	dec =''
	for i in range(n_lists):
		for j in range(len(key)):
			if i < len(lst[int(key[j])]):
				dec += enc[int(key[j])][i]
			else:
				None
	return dec



while choice != 0:
        choice = int(input('''

        $$ M E N U $$
    1) Encryption
    2) Decryption
    0) Exit

    Enter Your Choice?     '''))
        
        if choice != 0:
                with open("input.txt", 'r') as f:
                        msg = f.read()
                        f.close()
                #msg = "".join(input("\nEnter Message : ").split(" "))
                #print("msg : ",msg)
                n_lists = math.ceil(len(msg)/len(key))

        if choice == 1:
                enc(msg,key)
                print("\n\nEncryption using transpotion cipher is: ")
                enc_txt = ''
                for i in lst:
                        enc_txt += "".join(i)
                        print("".join(i),end=" ")

        elif choice == 2:
                dec_txt = dec(lst, key)
                print("\n\nDecryption using transpotion cipher is: ",end=" ")
                print(dec_txt)
        elif choice == 0:
                print("Thank You !!!!")
        else:
                print("INVALID CHOICE!!")

                
