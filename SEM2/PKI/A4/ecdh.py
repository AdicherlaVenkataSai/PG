# -*- coding: utf-8 -*-
"""ECDH.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/AdicherlaVenkataSai/SEM2/blob/master/PKI/A4/ECDH.ipynb

# key Agreement: client and server
"""

pip install tinyec

from tinyec import registry
# registry holds all the curves of elliptic curve
import secrets
# generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

curve = registry.get_curve('brainpoolP256r1')
# get_curve is used to pick one curve from the registry
print('curve  :', curve)
print('______________________________________________________________________________________________________________________________')
print('a value of curve :', curve.a)
print('b value of curve :',  curve.b)
print('generator point {x, y} :',  curve.field.g)
print('mod value of curve :',  curve.field.n)

"""let's consider A(client) and B(server) both
1. caluclate their private key between 1 and n-1(curve.field.n) using secrets library, info:`https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc`
2. cal the public key as publickey = private key * generator
(done use point addition or point doubling concept of ECC), info:`https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication`
3. ECC key agreement algorithms like ECDH
"""

APrivateKey = secrets.randbelow(curve.field.n)
# choosinng random number from 1 to n-1 
APublicKey = APrivateKey * curve.g
# cal the public key

BPrivateKey = secrets.randbelow(curve.field.n)
# choosinng random number from 1 to n-1 
BPublicKey =BPrivateKey * curve.g
# cal the public key


print('Private key of A :',APrivateKey)
print('Public key of A {x, y} :',APublicKey)
print(' \n Private key of B :',BPrivateKey)
print('Public key of B {x, y}:',BPublicKey)

"""note: Even though both the public key and generator are public to all, its difficult to calculate private key (discrete logarthmic problelm)"""

# A shared key is cal using its own privatekey and B public key 
ASharedKey = APrivateKey * BPublicKey

# B shared key is cal using its own privatekey and A public key 
BSharedKey = BPrivateKey * APublicKey

if(ASharedKey == BSharedKey):
  print('Keys are equal')
  print('The shared key {x, y} point :',ASharedKey)
  print('The shared key {x, y} point :',BSharedKey)
else:
  print('error')

'''print(" *********complete output *******")

print('curve  :', curve)
print('______________________________________________________________________________________________________________________________')
print('a value of curve :', curve.a)
print('b value of curve :',  curve.b)
print('generator point {x, y} :',  curve.field.g)
print('mod value of curve :',  curve.field.n)

print('Private key of A :',APrivateKey)
print('Public key of A {x, y} :',APublicKey)
print(' \n Private key of B :',BPrivateKey)
print('Public key of B {x, y}:',BPublicKey)

if(ASharedKey == BSharedKey):
  print('Keys are equal')
  print('The shared key {x, y} point :',ASharedKey)
  print('The shared key {x, y} point :',BSharedKey)
else:
  print('error')'''