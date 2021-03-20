with open("enc_test.txt", "r") as file:
    encode_text = file.read()

key = "strong_key"
decode_text = b""

for i in range(0, len(encode_text), len(key)):
    lol = bytes(ord(a) ^ ord(b) for a,b in zip(encode_text[i:i+len(key)], key))
    decode_text += lol

print(decode_text)

# with open("decoded.txt", "wb") as file:
#     file.write(decoded_text)
