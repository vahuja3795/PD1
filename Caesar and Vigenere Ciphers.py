# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:36:32 2018

@author: Varun Ahuja
"""
'''This function is encrypting a word/phrase using the Caesar Cipher.'''
def c_encrypt(x,y):
    uppercase = x.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = ''
    for z in range(len(x)):
        if uppercase[z] in letters:            
            name += letters[(letters.find(uppercase[z]) + y) % len(letters)]
        else:
            name += uppercase[z]
    return name

'''This function is decrypting a word/phrase using the Caesar Cipher.'''    
def c_decrypt(x,y):
    uppercase = x.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = ''
    for z in range (len(x)):
        if uppercase[z] in letters:
            name += letters[(letters.find(uppercase[z]) - y) % len(letters)]  
        else:
            name += uppercase[z]
    return name

'''This function is encrypting a word/phrase using the Vigenère Cipher.'''         
def vig_encrypt(x,y):
    uppercase = x.upper()
    uppercase1 = y.upper()
    index = 0
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = ''
    vig = []
    for z in uppercase:
        if z in letters:
            alpha = letters.find(z)
            alpha += letters.find(uppercase1[index])
            alpha %= len(letters)
            vig.append(letters[alpha])
            index += 1
            if index == len(uppercase1):
                index = 0
        else:
            vig.append(z)
    name = ''.join(vig)
    return name

'''This function is decrypting a word/phrase using the Vigenère Cipher.'''            
def vig_decrypt(x,y):
    uppercase = x.upper()
    uppercase1 = y.upper()
    index = 0
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = ''
    vig = []
    for z in uppercase:
        if z in letters:
            alpha = letters.find(z)
            alpha -= letters.find(uppercase1[index])
            alpha %= len(letters)
            vig.append(letters[alpha])
            index += 1
            if index == len(uppercase1):
                index = 0
        else:
            vig.append(z)
    name = ''.join(vig)
    return name