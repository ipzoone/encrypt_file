import os
import shutil
import sys
from tkinter import Tk, filedialog
from cryptography.fernet import Fernet

# ================ KONFIGURASI ================
VERSION = "3.1"
FILE_EXTENSION = ".ipzone"
ENCRYPTED_FOLDER_SUFFIX = " by ipzoneX"
KEY_FILE = "filekey.key"

# ================ UTILITIES ================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    VERSION = "1.0"  
    BLUE = '\033[0;34m'
    RED = '\033[31m'
    RESET = '\033[0m'

    banner = f"""
    {RED}============================={BLUE}
  _                               
 (_)                              
  _ _ __ _______  _ __   _____  __
 | | '_ \_  / _ \| '_ \ / _ \ \/ /
 | | |_) / / (_) | | | |  __/>  < 
 |_| .__/___\___/|_| |_|\___/_/\_\\
   | |                            
   |_|                            
   {RESET}{RED}
    IPZone Encryptor
    Version: {VERSION}
    ==============================
    Tools by {BLUE}ipzonex{RESET}{RED}
    Instagram:{BLUE}@ipzonex{RESET}{RED}
    Github: {BLUE}ipzoone{RESET}{RED}
    Linkedin: {BLUE}Saif Ali Mushaddiq{RESET}{RED}
<<<<<<< HEAD
    ================================={RESET}
=======
    ==============================={RESET}
>>>>>>> f1ae9c6402d9158d7743f6f5811afafc48b15241
    """
    print(banner)

# ================ KEY MANAGEMENT ================
def generate_key():
    """Membuat kunci baru dan menyimpan ke file"""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("\nKunci berhasil dibuat!")
    print("====================================")
    print(f"Kunci Anda: {key.decode()}")
    print("====================================")
    print("Simpan kunci ini di tempat AMAN!")

def load_key():
    """Memuat kunci dari file"""
    if not os.path.exists(KEY_FILE):
        print("Error: File kunci tidak ditemukan!")
        return None
    
    with open(KEY_FILE, "rb") as f:
        return f.read()

# ================ ENCRYPTION ================
def encrypt_folder(folder_path: str):
    """Mengenkripsi folder dengan kunci dari file"""
    try:
        key = load_key()
        if not key:
            return False

        cipher = Fernet(key)
        encrypted_folder = folder_path + ENCRYPTED_FOLDER_SUFFIX
        
        # Enkripsi semua file
        for root, _, files in os.walk(folder_path):
            for file in files:
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_path, folder_path)
                dest_path = os.path.join(encrypted_folder, relative_path + FILE_EXTENSION)
                
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                with open(src_path, "rb") as f:
                    data = f.read()
                
                with open(dest_path, "wb") as f:
                    f.write(cipher.encrypt(data))
        
        shutil.rmtree(folder_path)
        print(f"\nEnkripsi berhasil! Folder asli dihapus.")
        print(f"Folder terenkripsi: {encrypted_folder}")
    
    except Exception as e:
        print(f"\nError: {str(e)}")

# ================ DECRYPTION ================
def decrypt_folder(folder_path: str):
    """Mendekripsi folder dengan kunci manual"""
    try:
        # Minta kunci dari pengguna
        key_input = input("Masukkan kunci untuk dekripsi: ").strip().encode()
        
        # Baca kunci dari file
        stored_key = load_key()
        if not stored_key:
            return False
        
        # Validasi kunci
        if key_input != stored_key:
            print("\nError: Kunci yang dimasukkan tidak sesuai!")
            return False

        cipher = Fernet(stored_key)
        decrypted_folder = folder_path.replace(ENCRYPTED_FOLDER_SUFFIX, "")
        
        # Dekripsi semua file
        for root, _, files in os.walk(folder_path):
            for file in files:
                if not file.endswith(FILE_EXTENSION):
                    continue
                
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_path, folder_path)
                dest_path = os.path.join(decrypted_folder, relative_path.replace(FILE_EXTENSION, ""))
                
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                with open(src_path, "rb") as f:
                    data = f.read()
                
                with open(dest_path, "wb") as f:
                    f.write(cipher.decrypt(data))
        
        shutil.rmtree(folder_path)
        print(f"\nDekripsi berhasil! Folder terenkripsi dihapus.")
        print(f"Folder asli: {decrypted_folder}")
    
    except Exception as e:
        print(f"\nError: {str(e)}")

# ================ USER INTERFACE ================
def select_folder():
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    root.destroy()
    return folder

def main_menu():
    clear_screen()
    show_banner()
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Generate Key Baru")
        print("2. Enkripsi Folder")
        print("3. Dekripsi Folder")
        print("4. Exit")
        
        choice = input("Pilih opsi (1-4):").strip()

        if choice == "1":
            generate_key()
        elif choice == "2":
            if (folder := select_folder()) and os.path.exists(folder):
                encrypt_folder(folder)
        elif choice == "3":
            if (folder := select_folder()) and os.path.exists(folder):
                decrypt_folder(folder)
        elif choice == "4":
            print('''
<<<<<<< HEAD
                  \nTerima kasih telah menggunakan IPZone Encryptor!
                  ./IPZONEX
                  ''')
=======
            \nTerima kasih telah menggunakan IPZone Encryptor!
            ./IPZONEX
            ''')
>>>>>>> f1ae9c6402d9158d7743f6f5811afafc48b15241
            sys.exit(0)
        else:
            print("Input tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")
        clear_screen()

# ================ MAIN ================
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan oleh pengguna!")
        sys.exit(1)
