# Function to apply Caesar cipher decryption
def caesar_decrypt(cipher_text, shift):
    decrypted = []
    for char in cipher_text:
        if char.isalpha():
            # Decrypt character with the given shift and wrap around the alphabet
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted.append(shifted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Cipher text provided
cipher_text = "squiqhyiiycfbudeduutvehrhkjki"

# Trying all possible shifts (0 to 25)
for shift in range(26):
    decrypted_text = caesar_decrypt(cipher_text, shift)
    print(f"Shift {shift}: {decrypted_text}")
