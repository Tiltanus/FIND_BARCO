import random

def passGen(number, length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    passwords = {}
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        passwords[n]=password
    return passwords

def onePassGen(length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password
