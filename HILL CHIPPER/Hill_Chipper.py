
def create_matrix_from(key):
    m = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m

def encrypt(P, K):
    C = [0, 0, 0]
    C[0] = (K[0][0]*P[0] + K[1][0]*P[1] + K[2][0]*P[2]) % 26
    C[1] = (K[0][1]*P[0] + K[1][1]*P[1] + K[2][1]*P[2]) % 26
    C[2] = (K[0][2]*P[0] + K[1][2]*P[1] + K[2][2]*P[2]) % 26
    return C

def Hill(message, key):
    cipher_text = []
    K = create_matrix_from(key)
    for i in range(0, len(message), 3):
        P = [0, 0, 0]
        for j in range(3):
            if i+j < len(message):
                P[j] = ord(message[i+j]) % 65
        C = encrypt(P, K)
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
    return "".join(cipher_text)

# Contoh penggunaan
message ="akhdanfahr"
key = "GYBNQKURP"
cipher_text = Hill(message, key)
print("Plaintext: ", message)
print("Key: ", key)
print("Ciphertext: ", cipher_text)
