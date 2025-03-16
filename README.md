#**IPZONEX** Encryptor

IPZone Encryptor adalah alat enkripsi folder berbasis Python yang menggunakan algoritma **Fernet (AES-128)** dari pustaka **cryptography** untuk mengamankan file Anda. Alat ini memungkinkan Anda untuk mengenkripsi dan mendekripsi folder dengan mudah serta menyimpan kunci enkripsi untuk keamanan data, pastikan menggunakannya dengan legal.

---

## 🚀 Fitur
- 🔑 **Generate Key**: Membuat kunci enkripsi baru untuk mengenkripsi file.
- 🔒 **Enkripsi Folder**: Mengenkripsi semua file dalam folder yang dipilih.
- 🔓 **Dekripsi Folder**: Mendekripsi folder yang telah dienkripsi dengan kunci yang benar.
- 📂 **GUI Folder Selection**: Memudahkan pemilihan folder melalui dialog interaktif.
- 🗑️ **Menghapus Folder Asli**: Secara otomatis menghapus folder asli setelah enkripsi.

---

## 🛠️ Instalasi
Sebelum menjalankan program, pastikan Anda telah menginstal dependensi yang dibutuhkan.

```sh
pip install cryptography
```

Lalu, unduh atau clone repositori ini:

```sh
https://github.com/ipzoone/encrypt_file.git
```

---

## 🔧 Cara Penggunaan nya

### 1. Jalankan Program
```sh
python encryptX.0.1.py
```

### 2. Menu Utama
Saat program dijalankan, Anda akan melihat menu berikut:
```
=== MAIN MENU ===
1. Generate Key Baru
2. Enkripsi Folder
3. Dekripsi Folder
4. Exit
```

- **Generate Key Baru** → Buat kunci enkripsi dan simpan dalam `filekey.key`.
- **Enkripsi Folder** → Pilih folder untuk dienkripsi (file asli akan dihapus setelah enkripsi).
- **Dekripsi Folder** → Pilih folder terenkripsi untuk didekripsi (dengan memasukkan kunci yang benar).
- **Exit** → Keluar dari program.

### 3. Enkripsi Folder
- Pilih opsi `2. Enkripsi Folder`.
- Pilih folder melalui GUI.
- Semua file dalam folder akan dienkripsi dan dipindahkan ke folder baru dengan suffix **" by ipzoneX"**.
- Folder asli akan dihapus setelah proses selesai.

### 4. Dekripsi Folder
- Pilih opsi `3. Dekripsi Folder`.
- Masukkan kunci enkripsi yang benar.
- Semua file akan dikembalikan ke bentuk aslinya, dan folder terenkripsi akan dihapus.

---

## 📌 Catatan Penting
- **Simpan file `filekey.key` dengan aman!** Jika Anda kehilangan kunci ini, Anda tidak dapat mendekripsi file Anda.
- Setelah enkripsi selesai, folder asli akan dihapus. Pastikan Anda memiliki cadangan sebelum menjalankan program.
- Program ini hanya mengenkripsi isi file, bukan nama atau struktur foldernya.

---

## ⚠️ Disclaimer
IPZone Encryptor dibuat untuk penggunaan pribadi dan edukasi. Penggunaan alat ini untuk mengenkripsi atau mendekripsi file di komputer orang lain tanpa izin adalah **tindakan ilegal** dan bertentangan dengan hukum. Pengguna bertanggung jawab penuh atas penggunaan alat ini. Gunakan hanya pada komputer atau perangkat milik sendiri!

---

## 📞 Kontak
- **Instagram**: [@ipzonex](https://instagram.com/ipzonex)
- **GitHub**: [ipzoone](https://github.com/ipzoone)
- **LinkedIn**: [Saif Ali Mushaddiq](https://linkedin.com/in/saif-ali-mushaddiq)

**./IPZONEX** Terima kasih telah menggunakan IPZone Encryptor gunakan secara legal ya, etika di atas segala nya! 😊

