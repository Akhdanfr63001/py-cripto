def vigenere_cipher(text, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            key_char = key[i % key_length].lower()
            shift = (ord(char) - ord('a') + ord(key_char) - ord('a')) % 26
            shifted_char = chr(ord('a') + shift)
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

def main():
    text = input("Masukkan teks yang akan dienkripsi: ")
    key = input("Masukkan kunci enkripsi: ")
    encrypted_text = vigenere_cipher(text, key)
    print("Teks terenkripsi:", encrypted_text)

if __name__ == "__main__":
    main()
