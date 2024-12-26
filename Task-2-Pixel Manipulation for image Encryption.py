import numpy as np
from PIL import Image
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img) 
    encrypted_array = (img_array + key) % 256 
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    decrypted_array = (img_array - key) % 256  
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")
print("** Pro Image Encryption Tool **")
key = int(input("Enter a numeric key for encryption: "))
input_path = input("Enter the path of the image to encrypt: ")
output_path_encrypted = "pro_encrypted_image.png"
encrypt_image(input_path, output_path_encrypted, key)
output_path_decrypted = "pro_decrypted_image.png"
decrypt_image(output_path_encrypted, output_path_decrypted, key)


