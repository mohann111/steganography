# Secure Data Hiding in Image Using Steganography  

## Overview  
This project implements image steganography using Python and OpenCV, allowing secure data hiding within PNG images. The encryption process hides text data inside an image, while the decryption process retrieves the hidden data using a password for authentication.  

## Features  
- Hide secret text messages inside PNG images  
- Extract hidden text from steganographic images with password verification  
- Uses OpenCV for image processing  
- SHA-256 hashing for password-based authentication  
- Separate encryption and decryption modules  

## Technologies Used  
- Python  
- OpenCV  
- NumPy  
- Hashlib (for password hashing)  

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/mohann111/steganography.git
   ```
2. Install dependencies:  
   ```bash
   pip install opencv-python numpy
   ```

## Usage  

### Hiding Data (Encryption)  
Run the encryption script to hide a message in an image:  
```bash
python encrypt.py input.png "Your secret message" output.png
```
You will be prompted to enter a password to secure the hidden message.

### Extracting Data (Decryption)  
Run the decryption script to extract the hidden message:  
```bash
python decrypt.py output.png
```
You will need to enter the correct password to retrieve the message successfully.

## How It Works  
- The script modifies the least significant bits (LSB) of pixel values to encode text data.  
- A **SHA-256 hash of the password** is stored alongside the message to verify authentication during decryption.  
- The modified image looks visually identical to the original.  
- The extraction process reads the modified pixel values, verifies the password, and reconstructs the hidden message.  

## Example  
**Original Image:**  
📷 `input.png`  

**After Encryption:**  
📷 `output.png` (visually identical but contains hidden data)  

**Decryption with Correct Password:**  
📝 "Your secret message"  

## License  
This project is licensed under the MIT License.  


