def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_cipher_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                encrypted_text += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def affine_cipher_decrypt(ciphertext, a, b):
    decrypted_text = ""
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "Kunci tidak valid. a tidak memiliki invers modulo 26."
    
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr(((a_inverse * (ord(char) - ord('a') - b)) % 26) + ord('a'))
            else:
                decrypted_text += chr(((a_inverse * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Contoh penggunaan
plaintext = "Hello, World!"
a = 3
b = 7

encrypted_text = affine_cipher_encrypt(plaintext, a, b)
decrypted_text = affine_cipher_decrypt(encrypted_text, a, b)

print("Plaintext: ", plaintext)
print("Enkripsi: ", encrypted_text)
print("Dekripsi: ", decrypted_text)
