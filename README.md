# 📝 Encrypted Notepad App

A secure personal notepad application built with Python that allows users to add, view, edit, and delete encrypted notes. Each note is protected using a **master password** and encrypted using the **Fernet encryption scheme** from the `cryptography` module.

---

## 🔐 Features

- ✍️ Create, edit, and delete notes  
- 🔑 Master password authentication  
- 🔒 End-to-end encryption using Fernet (symmetric encryption)  
- 🗂 Multiple notes with titles  
- 💾 Auto-save & view notes from dashboard  
- 🎨 Minimal GUI with modern Notepad-style interface

---

## 🚀 Technologies Used

- Python 3.x  
- cryptography (Fernet)  
- Tkinter / CustomTkinter *(optional for GUI)*  
- OS, JSON, base64 modules

---

## 📁 Folder Structure
encrypted_notepad/
│
├── main.py # Launch file
├── notes/ # Encrypted notes stored here
├── master.key # Master password (hashed/encrypted)
├── utils.py # Encryption/decryption logic
└── README.md
## ⚙️ How to Run

### 🔧 1. Install Dependencies

```bash
pip install cryptography

2. Run the App
bash
Copy code
python main.py
3.if using gui
python gui_notepad.py

