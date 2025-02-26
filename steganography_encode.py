import cv2
import numpy as np
import hashlib

def encode_text_to_image(image_path, text, password, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or cannot be loaded!")
        return
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    text = password_hash + text + "EOF"  # Store hashed password with the message
    
    binary_text = ''.join(format(ord(c), '08b') for c in text)  # Convert text to binary
    binary_text += '0' * (8 - len(binary_text) % 8)  # Ensure it is a multiple of 8
    
    data_index = 0
    data_length = len(binary_text)

    height, width, _ = img.shape
    if data_length > height * width * 3:
        print("Error: Message is too large for the image!")
        return

    for i in range(height):
        for j in range(width):
            for channel in range(3):  # Iterate over BGR channels
                if data_index < data_length:
                    img[i, j, channel] = (img[i, j, channel] & 0b11111110) | int(binary_text[data_index])  # Modify LSB
                    data_index += 1

    cv2.imwrite(output_path, img)  # Save as PNG to prevent compression loss
    print(f"Text successfully hidden in {output_path}")

if __name__ == "__main__":
    input_image = "tinku.png"  # Use PNG to ensure lossless encoding
    output_image = "encryptedImage.png"
    secret_message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encode_text_to_image(input_image, secret_message, password, output_image)
