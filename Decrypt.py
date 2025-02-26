import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import ttk, messagebox

def bits_to_int(bits):
    return int("".join(map(str, bits)), 2)

def bits_to_str(bits):
    bytes_list = [bits[i:i + 8] for i in range(0, len(bits), 8)]
    chars = [chr(bits_to_int(byte)) for byte in bytes_list]
    return "".join(chars)

def extract_header(bits):
    passcode_len = bits_to_int(bits[:16])
    passcode_bits = bits[16:16 + passcode_len * 8]
    passcode = bits_to_str(passcode_bits)
    message_len = bits_to_int(bits[16 + passcode_len * 8:16 + passcode_len * 8 + 32])
    message_start = 16 + passcode_len * 8 + 32
    return passcode, message_len, message_start

def extract_message(bits, message_len, message_start):
    message_bits = bits[message_start:message_start + message_len * 8]
    return bits_to_str(message_bits)

def decrypt():
    img_path = "encrypted.png"
    if not os.path.exists(img_path):
        messagebox.showerror("Error", "Encrypted image 'encrypted.png' not found!")
        return

    image = cv2.imread(img_path)
    if image is None:
        messagebox.showerror("Error", "Failed to load 'encrypted.png'.")
        return

    bits = [pixel & 1 for pixel in image.flatten()]
    stored_passcode, message_len, message_start = extract_header(bits)

    if passcode_entry.get() != stored_passcode:
        messagebox.showerror("Error", "Incorrect passcode!")
        return

    secret_message = extract_message(bits, message_len, message_start)
    secret_message_label.config(text=f"Secret Message: {secret_message}")

def setup_gui():
    root = tk.Tk()
    root.title("Steganography - Decrypt")
    root.geometry("400x300")

    style = ttk.Style(root)
    style.theme_use('clam')

    frame = ttk.Frame(root, padding="20")
    frame.pack(expand=True)

    ttk.Label(frame, text="Enter Passcode:").grid(row=0, column=0, sticky="w", pady=5)
    passcode_entry = ttk.Entry(frame, width=40, show="*")
    passcode_entry.grid(row=1, column=0, pady=5)

    decrypt_button = ttk.Button(frame, text="Decrypt", command=decrypt)
    decrypt_button.grid(row=2, column=0, pady=10)

    secret_message_label = ttk.Label(frame, text="Secret Message: ", wraplength=350)
    secret_message_label.grid(row=3, column=0, pady=10)

    return root, passcode_entry, secret_message_label

if _name_ == "_main_":
    root, passcode_entry, secret_message_label = setup_gui()
    root.mainloop()