# 🔒 Secure Data Hiding in Images using Steganography

## 📖 Overview
This project provides a user-friendly GUI application to **encrypt and decrypt secret messages within images** using **steganography**. By leveraging the least significant bit (LSB) technique, the system securely hides data without visibly altering the original image.

## 🚀 Features
- 🔐 **Encryption Module:** Embed secret messages into images with a passcode.  
- 🔓 **Decryption Module:** Extract hidden messages by verifying the passcode.  
- 🖼️ **Supports common image formats** like `.jpg` and `.png`.  
- 🧩 **User-friendly GUI** built with `tkinter`.  
- 📎 **Passcode protection** for enhanced security.  

---

## 🛠️ Technologies Used
- **Python** 🐍  
- **OpenCV** 📷 *(for image processing)*  
- **NumPy** 🔢 *(for efficient array handling)*  
- **Tkinter** 🖥️ *(for GUI development)*  

---

## 📂 Project Structure
```
📁 Secure-Data-Hiding-in-Images-using-Steganography
├── Encrypt.py       # Encrypts and hides messages in images
├── Decrypt.py       # Extracts hidden messages from images
├── mypic.jpg        # Input image for encryption (user-provided)
├── encrypted.png    # Output image with hidden message
└── README.md        # Project documentation
```

---

## 🔧 Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/Secure-Data-Hiding-in-Images-using-Steganography.git
cd Secure-Data-Hiding-in-Images-using-Steganography
```

### 2️⃣ **Install Dependencies**
Make sure you have **Python 3.7+** installed, then run:
```bash
pip install opencv-python numpy
```

> 💡 *Tkinter is included with most Python installations. If not, install it separately.*  

---

## 🖥️ How to Use

### 🔐 **Encryption Process (`Encrypt.py`):**  
1. Place your **input image** as `mypic.jpg` in the project directory.  
2. Run the encryption script:  
   ```bash
   python Encrypt.py
   ```  
3. In the GUI window:  
   - Enter your **secret message**.  
   - Provide a **passcode** for added security.  
   - Click **Encrypt** to generate `encrypted.png`.  

---

### 🔓 **Decryption Process (`Decrypt.py`):**  
1. Ensure `encrypted.png` is present in the project folder.  
2. Run the decryption script:  
   ```bash
   python Decrypt.py
   ```  
3. In the GUI:  
   - Enter the correct **passcode**.  
   - Click **Decrypt** to reveal the hidden message.  

---


## 📝 To-Do / Future Enhancements
- [ ] Support for **multiple image formats** (BMP, TIFF)  
- [ ] **Improved encryption algorithms** for added security  
- [ ] Drag-and-drop image functionality in GUI 🖱️  
- [ ] Cross-platform packaging with **PyInstaller**  

---

## ⚠️ Limitations
- Large messages may exceed the embedding capacity of smaller images.  
- Currently supports **only RGB images**.  

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify it! 🚀  

---


⭐ **If you find this project helpful, consider giving it a star!** ⭐  
```

---

### ✅ **Instructions:**  
1. **Save the content above as `README.md`** in your project folder.  
2. **Replace `your-username`** with your actual GitHub username.  
3. **Add demo screenshots** by replacing the placeholder links.  
4. **Push to GitHub:**  
   ```bash
   git add .
   git commit -m "Add README for steganography project"
   git push origin main
   ```

Would you like me to include **badges** (e.g., Python version, GitHub stars)? 😊
