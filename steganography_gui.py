import cv2
import numpy as np
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def encode_text_to_image(image_path, text, password, output_path):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Image not found or cannot be loaded!")
        return
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    text = password_hash + text + "EOF"
    
    binary_text = ''.join(format(ord(c), '08b') for c in text)
    binary_text += '0' * (8 - len(binary_text) % 8)
    
    data_index = 0
    data_length = len(binary_text)

    height, width, _ = img.shape
    if data_length > height * width * 3:
        messagebox.showerror("Error", "Message is too large for the image!")
        return

    for i in range(height):
        for j in range(width):
            for channel in range(3):
                if data_index < data_length:
                    img[i, j, channel] = (img[i, j, channel] & 0b11111110) | int(binary_text[data_index])
                    data_index += 1

    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", f"Text successfully hidden in {output_path}") 
def decode_text_from_image(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Encrypted image not found!")
        return
    
    binary_text = ""
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for channel in range(3):
                binary_text += str(img[i, j, channel] & 1)

    decoded_chars = [chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8)]
    message = ''.join(decoded_chars)
    
    if "EOF" in message:
        message = message[:message.index("EOF")]
        stored_password_hash = message[:64]
        message = message[64:]
        
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()
        if stored_password_hash == input_password_hash:
            messagebox.showinfo("Decryption Success", f"Message: {message}")
        else:
            messagebox.showerror("Error", "Incorrect password!")
    else:
        messagebox.showerror("Error", "No valid hidden message found!")

def browse_file(entry):
    filename = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def encode_ui():
    root = tk.Tk()
    root.title("Steganography - Encode")
    
    tk.Label(root, text="Image Path:").grid(row=0, column=0)
    img_entry = tk.Entry(root, width=50)
    img_entry.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=lambda: browse_file(img_entry)).grid(row=0, column=2)
    
    tk.Label(root, text="Secret Message:").grid(row=1, column=0)
    text_entry = tk.Entry(root, width=50)
    text_entry.grid(row=1, column=1, columnspan=2)
    
    tk.Label(root, text="Password:").grid(row=2, column=0)
    pass_entry = tk.Entry(root, width=50, show="*")
    pass_entry.grid(row=2, column=1, columnspan=2)
    
    tk.Button(root, text="Encode", command=lambda: encode_text_to_image(img_entry.get(), text_entry.get(), pass_entry.get(), "encoded.png")).grid(row=3, column=1)
    
    root.mainloop()

def decode_ui():
    root = tk.Tk()
    root.title("Steganography - Decode")
    
    tk.Label(root, text="Encrypted Image Path:").grid(row=0, column=0)
    img_entry = tk.Entry(root, width=50)
    img_entry.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=lambda: browse_file(img_entry)).grid(row=0, column=2)
    
    tk.Label(root, text="Password:").grid(row=1, column=0)
    pass_entry = tk.Entry(root, width=50, show="*")
    pass_entry.grid(row=1, column=1, columnspan=2)
    
    tk.Button(root, text="Decode", command=lambda: decode_text_from_image(img_entry.get(), pass_entry.get())).grid(row=2, column=1)
    
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Steganography - Main")
    
    tk.Label(root, text="Choose an Option:").pack()
    tk.Button(root, text="Encode Message", command=encode_ui).pack()
    tk.Button(root, text="Decode Message", command=decode_ui).pack()
    
    root.mainloop()
