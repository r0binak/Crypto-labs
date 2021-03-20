with open("dec_test.txt", "r") as file:
    decode_text = file.read()[:-1] #открытие файла и считывание в переменную без переноса строки

key = "strong_key"
sooooooo_encoded = b""

for i in range(0, len(decode_text), len(key)): #цикл от 0 до длины текста с шагом длинны ключа
    qwerty_param = bytes(ord(a) ^ ord(b) for a,b in zip(decode_text[i:i+len(key)], key)) #xor между байтами текста и ключа
    sooooooo_encoded += qwerty_param #мультибайтовый XOR

print(sooooooo_encoded)

with open("enc_test.txt", "wb") as file:
    file.write(sooooooo_encoded)
