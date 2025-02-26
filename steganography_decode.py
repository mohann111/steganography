import cv2
import numpy as np
import hashlib

def decode_text_from_image(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Encrypted image not found!")
        return
    
    binary_text = ""
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for channel in range(3):  # Iterate over BGR channels
                binary_text += str(img[i, j, channel] & 1)  # Extract LSB

    decoded_chars = [chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8)]
    message = ''.join(decoded_chars)
    
    if "EOF" in message:
        message = message[:message.index("EOF")]
        stored_password_hash = message[:64]  # Extract stored password hash
        message = message[64:]  # Extract actual hidden message
        
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()
        if stored_password_hash == input_password_hash:
            print("Decryption message:", message)
        else:
            print("Error: Incorrect password!")
    else:
        print("Error: No valid hidden message found!")

if __name__ == "__main__":
    encrypted_image = "encryptedImage.png"  # Use PNG for decoding
    password = input("Enter passcode for decryption: ")
    decode_text_from_image(encrypted_image, password)
