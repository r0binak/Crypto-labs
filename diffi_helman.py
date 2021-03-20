import random
import hashlib
import sys

g=3
p=953

a=random.randint(5, 10)

b=random.randint(10,20)

A = (g**a) % p
B = (g**b) % p

print('  ____  ____  ____  ____  ____           _   _  ____  __    __    __  __    __    _  _') 
print(' (  _ \(_  _)( ___)( ___)(_  _)   ___   ( )_( )( ___)(  )  (  )  (  \/  )  /__\  ( \( )')
print('  )(_) )_)(_  )__)  )__)  _)(_   (___)   ) _ (  )__)  )(__  )(__  )    (  /(__)\  )  ( ')
print(' (____/(____)(__)  (__)  (____)         (_) (_)(____)(____)(____)(_/\/\_)(__)(__)(_)\_)')

print('\ng:',g,' (первообразный корень по модулю p, простое число), p:',p, ' (простое число)') #известные числа

print('\nАлиса посчитала:')
print('a (случайное число Алисы): ',a)
print('Значение Алисы (A): ',A,' (g^a) mod p') 

print('\nБоб посчитал:')
print('b (случайное число Боба): ',b)
print('Значение Боба (B): ',B,' (g^b) mod p')

print('\nАлиса посчитала:')
keyA=(B**a) % p
print('Ключ: ',keyA,' (B^a) mod p')
print('Ключ: ',hashlib.sha256(str(keyA).encode()).hexdigest())

print('\nБоб посчитал:')
keyB=(A**b) % p
print('Ключ: ',keyB,' (A^b) mod p')
print('Ключ: ',hashlib.sha256(str(keyB).encode()).hexdigest())