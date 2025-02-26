
# Secure Data Hiding in Image Using Steganography  

## Overview  
This project implements image steganography using Python and OpenCV, allowing secure data hiding within PNG images. The encryption process hides text data inside an image, while the decryption process retrieves the hidden data.  

## Features  
- Hide secret text messages inside PNG images  
- Extract hidden text from steganographic images  
- Uses OpenCV for image processing  
- Separate encryption and decryption modules  

## Technologies Used  
- Python  
- OpenCV  
- NumPy  

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/mohann111/stenography.git
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

### Extracting Data (Decryption)  
Run the decryption script to extract the hidden message:  
```bash
python decrypt.py output.png
```

## How It Works  
- The script modifies the least significant bits (LSB) of pixel values to encode text data.  
- The modified image looks visually identical to the original.  
- The extraction process reads the modified pixel values and reconstructs the hidden message.  

## Example  
**Original Image:**  
📷 `input.png`  

**After Encryption:**  
📷 `output.png` (visually identical but contains hidden data)  

**Extracted Message:**  
📝 "Your secret message"  

## License  
This project is licensed under the MIT License.  

---

Let me know if you need any modifications! 🚀
