import random
import string

def main():
    chars = " " + string.punctuation + string.digits + string.ascii_letters # string. is a simple way to add get characters, punctuation and ascii letters

    chars = list(chars) # you can turn a string into a list of chars, but not the other way around
    key = chars.copy()

    random.shuffle(key)

    print(f"chars: {chars}")
    print(f"key: {key}")

    # Encrypt

    plainMessage = input("Enter a message you would like to encode: ")
    encryptedMessage = ""

    for char in plainMessage:
        encryptedMessage += key[chars.index(char)]

    print(f"Encrypted message: {encryptedMessage}")

    # Decrypt

    originalMessage = input("Enter a message you would like to decode: ")
    decryptedMessage = ""

    for char in originalMessage:
        decryptedMessage += chars[key.index(char)]

    print(f"Decrypted message: {decryptedMessage}")

if __name__ == "__main__":
    main()