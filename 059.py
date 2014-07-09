#!/usr/bin/env python
#coding:utf-8

"""

XOR decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

"""

'''
A 8.19 B 1.47 C 3.83 D 3.91 E 12.25 F 2.26 G 1.71 
H 4.57 I 7.10 J 0.14 K 0.41 L 3.77 M 3.34 N 7.06 
O 7.26 P 2.89 Q 0.09 R 6.85 S 6.36 T 9.41 
U 2.58 V 1.09 W 1.59 X 0.21 Y 1.58 Z 0.08
'''
def most(arr):
	return max(map(lambda x:(arr.count(x),x),arr))[1]

def answer():
	f=open('cipher1.txt','r')
	ciphers=f.read().replace('\n','').split(',')
	a=[ciphers[i] for i in xrange(len(ciphers)) if i%3==0]
	b=[ciphers[i] for i in xrange(len(ciphers)) if i%3==1]
	c=[ciphers[i] for i in xrange(len(ciphers)) if i%3==2]
	key=''.join([chr(int(most(i))^ord(' ')) for i in [a,b,c]])
	plain_text=[int(ciphers[i])^ord(key[i%len(key)]) for i in xrange(len(ciphers))]
	print 'Answer is',sum(plain_text)
	print '='*80
	print 'Decrypted message:'
	print ''.join([chr(i) for i in plain_text])

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 107359
# run time= 0.0108640193939