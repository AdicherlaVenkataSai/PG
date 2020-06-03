import hashlib
import itertools
import time

d = {}

#comb = combinations([0,1], 2)


l = list(itertools.product([0,1], repeat=6))

start_time = time.time()

for i in list(l):
	s = ''
	s = str(i[0])+str(i[1])+str(i[2])+str(i[3])+str(i[4])+str(i[5])
	#print(s)
	#print(i)

	m = hashlib.md5(s.encode())
	val = m.hexdigest()
	#print('Using MD5 Hash Function: ',val[0:3])
	print(s, '->', val)
	if val[0:3] not in d.keys():
		d[val[0:3]] = s
	else:
		print('\nCollision detected for binary number ->', s, ', hexdigest value ->', val)
		m1 = hashlib.md5(d[val[0:3]].encode())
		print('\nPrevious stored binary number ->', d[val[0:3]], ', hexdigest value ->', m1.hexdigest())
		end_time = time.time() 
		print('\nTime required for Collision detection ->', end_time - start_time, 'Seconds')
		break