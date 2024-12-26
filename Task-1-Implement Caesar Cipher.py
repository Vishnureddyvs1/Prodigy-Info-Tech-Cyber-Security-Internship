def caesar_cipher(text, shift, mode="encrypt"):
    """
    Perform Caesar Cipher encryption or decryption
    """
    result = ""
    shift_amount = shift % 26 
    if mode == "decrypt":
        shift_amount = -shift_amount  
    for char in text:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')  
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += new_char
        else:
            result += char 
    return result
print("** Welcome To Caesar Cipher Program In Simple Way **")
message = input("Enter your message: ").strip()
shift = int(input("Enter the shift value: "))
encrypted_message = caesar_cipher(message, shift, mode="encrypt")
print(f"Encrypted message: {encrypted_message}")
decrypted_message = caesar_cipher(encrypted_message, shift, mode="decrypt")
print(f"Decrypted message: {decrypted_message}")

