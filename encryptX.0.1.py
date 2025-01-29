import os
import shutil
from tkinter import Tk, filedialog
from cryptography.fernet import Fernet
import sys
import base64

banner = """


                                                             $$\     $$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$\   $$\ 
                                                             $$ |    \____$$  |$$  __$$\ $$$\  $$ |$$  _____|$$ |  $$ |
 $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\ $$$$$$\       $$  / $$ /  $$ |$$$$\ $$ |$$ |      \$$\ $$  |
$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$ |  $$ |$$  __$$\\_$$  _|     $$  /  $$ |  $$ |$$ $$\$$ |$$$$$\     \$$$$  / 
$$$$$$$$ |$$ |  $$ |$$ /      $$ |  \__|$$ |  $$ |$$ /  $$ | $$ |      $$  /   $$ |  $$ |$$ \$$$$ |$$  __|    $$  $$<  
$$   ____|$$ |  $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\  $$  /    $$ |  $$ |$$ |\$$$ |$$ |      $$  /\$$\ 
\$$$$$$$\ $$ |  $$ |\$$$$$$$\ $$ |      \$$$$$$$ |$$$$$$$  | \$$$$  |$$$$$$$$\  $$$$$$  |$$ | \$$ |$$$$$$$$\ $$ /  $$ |
 \_______|\__|  \__| \_______|\__|       \____$$ |$$  ____/   \____/ \________| \______/ \__|  \__|\________|\__|  \__|
                                        $$\   $$ |$$ |                                                                 
                                        \$$$$$$  |$$ |                                                                 
                                         \______/ \__|                                                                                                                                                                                                    
"""
print("\033[31m" + banner + "\033[0m")
print("""
      Tools by ipzonex
      Instagram : @ipzonex
      Github    : ipzoone
      Linkedin  : Saif Ali Mushaddiq
      """)
     

# Fungsi untuk membuat kunci dan menyimpannya ke file
def generate_key(key_file="filekey.key"):
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)
    print(f"Kunci berhasil disimpan di '{key_file}'")

# Fungsi untuk memuat kunci dari file
def load_key(key_file="filekey.key"):
    if not os.path.exists(key_file):
        print(f"File kunci '{key_file}' tidak ditemukan. Silakan buat kunci terlebih dahulu.")
        return None
    with open(key_file, "rb") as file:
        return file.read()

# Fungsi untuk mengenkripsi isi file
def encrypt_file(file_path, key, output_path):
    cipher_suite = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)

    # Simpan file terenkripsi
    with open(output_path, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{file_path}' berhasil dienkripsi menjadi '{output_path}'.")

# Fungsi untuk mendekripsi isi file
def decrypt_file(file_path, key, output_path):
    cipher_suite = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        # Simpan file hasil dekripsi
        with open(output_path, "wb") as file:
            file.write(decrypted_data)
        print(f"File '{file_path}' berhasil didekripsi menjadi '{output_path}'.")
    except Exception as e:
        print(f"Error: Gagal mendekripsi file '{file_path}'. Kunci salah atau file rusak. {e}")

# Fungsi untuk mengenkripsi folder
def encrypt_folder(folder_path, key):
    print(f"Mengenkripsi folder: {folder_path}...")
    encrypted_folder = folder_path + " by ipzoneX"
    os.makedirs(encrypted_folder, exist_ok=True)

    # Salin dan enkripsi setiap file di dalam folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            original_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(original_file_path, folder_path)
            encrypted_file_path = os.path.join(encrypted_folder, relative_path + ".ipzone")

            # Buat subfolder jika diperlukan
            os.makedirs(os.path.dirname(encrypted_file_path), exist_ok=True)
            encrypt_file(original_file_path, key, encrypted_file_path)

    # Buat file decrypt.exe untuk dekripsi
    create_decrypt_exe(encrypted_folder, key)

    # Hapus folder asli setelah enkripsi selesai
    shutil.rmtree(folder_path)
    print(f"Folder asli '{folder_path}' berhasil dienkripsi dan dihapus.")

# Fungsi untuk mendekripsi folder
def decrypt_folder(folder_path, key):
    print(f"Mendekripsi folder: {folder_path}...")
    decrypted_folder = folder_path.replace(" by ipzoneX", "")
    os.makedirs(decrypted_folder, exist_ok=True)

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ipzone"):
                encrypted_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(encrypted_file_path, folder_path)
                original_file_path = os.path.join(decrypted_folder, relative_path.replace(".ipzone", ""))

                # Buat subfolder jika diperlukan
                os.makedirs(os.path.dirname(original_file_path), exist_ok=True)
                print(f"Decrypting: {encrypted_file_path} -> {original_file_path}")
                decrypt_file(encrypted_file_path, key, original_file_path)

    print(f"Folder berhasil didekripsi ke '{decrypted_folder}'.")

# Fungsi untuk membuka dialog File Explorer di depan terminal
def select_folder():
    root = Tk()
    root.withdraw()  # Menyembunyikan jendela utama Tkinter
    root.attributes("-topmost", True)  # Membuat File Explorer muncul di depan terminal
    folder_path = filedialog.askdirectory()
    root.attributes("-topmost", False)  # Kembalikan normal setelah File Explorer selesai
    if not folder_path:
        print("Tidak ada folder yang dipilih.")
    return folder_path

# Fungsi untuk membuat file decrypt.exe
def create_decrypt_exe(folder, key):
    decrypt_code = f"""
import os
from cryptography.fernet import Fernet

def decrypt_file(file_path, key, output_path):
    cipher_suite = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        # Simpan file hasil dekripsi
        with open(output_path, "wb") as file:
            file.write(decrypted_data)
        print(f"File '{{file_path}}' berhasil didekripsi menjadi '{{output_path}}'.")
    except Exception as e:
        print(f"Error: Gagal mendekripsi file '{{file_path}}'. Kunci salah atau file rusak. {{e}}")

def decrypt_folder(folder_path, key):
    print(f"Mendekripsi folder: {{folder_path}}...")
    decrypted_folder = folder_path.replace(" by ipzoneX", "")
    os.makedirs(decrypted_folder, exist_ok=True)

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ipzone"):
                encrypted_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(encrypted_file_path, folder_path)
                original_file_path = os.path.join(decrypted_folder, relative_path.replace(".ipzone", ""))

                # Buat subfolder jika diperlukan
                os.makedirs(os.path.dirname(original_file_path), exist_ok=True)
                print(f"Decrypting: {{encrypted_file_path}} -> {{original_file_path}}")
                decrypt_file(encrypted_file_path, key, original_file_path)

    print(f"Folder berhasil didekripsi ke '{{decrypted_folder}}'.")

if __name__ == "__main__":
    # Masukkan kunci untuk dekripsi
    key_input = input("Masukkan kunci untuk mendekripsi: ").strip().encode()
    folder_path = input("Masukkan path folder yang ingin didekripsi: ").strip()
    decrypt_folder(folder_path, key_input)
"""
    exe_path = os.path.join(folder, "decrypt.exe")
    with open(exe_path, "w") as exe_file:
        exe_file.write(decrypt_code)
    print(f"File 'decrypt.exe' berhasil dibuat di folder: {folder}")

# Menu utama dengan loop
def main():
    while True:
        print("\n===================================")
        print("1. Buat kunci baru")
        print("2. Enkripsi folder")
        print("3. Dekripsi folder")
        print("4. Keluar")
        print("===================================")
        
        choice = input("Pilih opsi (1/2/3/4): ").strip()

        if choice == "1":
            generate_key()
        elif choice == "2":
            key = load_key()
            if not key:
                continue
            folder_path = select_folder()
            if not folder_path:
                print("Proses dibatalkan.")
                continue
            encrypt_folder(folder_path, key)
        elif choice == "3":
            key = input("Masukkan kunci: ").strip().encode()
            folder_path = select_folder()
            if not folder_path:
                print("Proses dibatalkan.")
                continue
            decrypt_folder(folder_path, key)
        elif choice == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
