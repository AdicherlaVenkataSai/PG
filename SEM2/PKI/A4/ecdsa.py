# -*- coding: utf-8 -*-
"""ECDSA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/AdicherlaVenkataSai/SEM2/blob/master/PKI/A4/ECDSA.ipynb

# Digital Signature

`https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm`
"""

pip install tinyec

from tinyec import registry
import hashlib, secrets, sys

def extendedEucledian(r1,r2):
    if r1 == 0:
        return (r2, 0, 1)
    else:
        gcd, x, y = extendedEucledian(r2 % r1, r1)
        return (gcd, y - (r2//r1) * x, x)

def sha3_256Hash(message):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")

"""Signature generation algorithm:
1. Calculate  e=HASH(m)
2. Let z be the L(n) leftmost bits of e, where L(n) is the bit length of the group order n.
3. Select a cryptographically secure random integer k from [1,n-1].
4. Calculate the curve point (x1,y1)=k *G.
5. Calculate r=x1 mod n. If r=0, go back to step 3.
6. Calculate  s=inverse(k)(e + r * private key). If s=0, go back to step 3.
7. The signature is the pair (r,s).and (r,-s mod n) is also a valid signature.

note: K should be secret, and we need to select different signatures, if not the private key value can be calculated 

`private key = (s * k - e) / r`
"""

def signECDSA(msg, privKey):
    msgHash = sha3_256Hash(msg)
    
    flag = True
    while flag:
        k_random =  secrets.randbelow(curve.field.n)
        new_curve_point = k_random * curve.g

        if new_curve_point.x != 0:
            flag = False
            r = new_curve_point.x % curve.field.n

    flag = True
    while flag:
        k_inv = extendedEucledian(k_random, curve.field.n)[1]
        s = (k_inv * (msgHash + r * privKey)) % curve.field.n

        if s != 0:
            flag = False

    return (r, s)

"""signature verifying algorithm:
1. Verify that r and s are integers in (1, n-1). If not, the signature is invalid.
2. Calculate e=HASH(m), where HASH is the same function used in the signature generation.
3. Let z be the L(n) leftmost bits of e.
4. Calculate u1=z * inverse(s) mod n and  u2=r * inverse(s) mod n
5. Calculate the curve point 
(x1,y1)=u1 x G + u2 x public key
If (x1,y1)=O then the signature is invalid.
6. The signature is valid if r == x1 mod n, invalid otherwise
"""

def verifyECDSA(msg, signature, pubKey):
    r, s = signature
    if r not in range(curve.field.n) and s not in range(curve.field.n): 
      print("\nInvalid Signature") 
      sys.exit(0)
    msgHash = sha3_256Hash(msg)
    s_inv = extendedEucledian(s, curve.field.n)[1]
    u1 = (msgHash * s_inv) % curve.field.n; u2 = (r * s_inv)% curve.field.n
    new_point = u1 * curve.g + u2 * pubKey

    return True if new_point.x == r % curve.field.n else False

msg = 'doing assigments by borrowing laptop form neighbours'
curve = registry.get_curve('brainpoolP256r1')

privKey = secrets.randbelow(curve.field.n)


pubKey = privKey * curve.g


signature = signECDSA(msg, privKey)
print('\nMessage: ', msg)
print('\nPrivate key: ', privKey)
print('public key point (x, y): ', pubKey.x, "\n", pubKey.y)
print('nSignature: r= :' + hex(signature[0]) + '\ns= : ' + hex(signature[1]))

verifying = verifyECDSA(msg, signature, pubKey)
print('Actual Message: ', msg)
print('Is Signature Valid ', verifying)

msg = 'qwertyuio'
verifying = verifyECDSA(msg, signature, pubKey)
print('Message:', msg)
print('Is Signature Valid ', valid)