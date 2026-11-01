
# Program Analisis Nilai Mahasiswa

## 1. Identitas
- Nama: Hana Karimah Ghoziyah
- NIM: 2225250165
- Kelas: 3B
- Mata Kuliah: Algoritma dan Pemrograman

## 2. Deskripsi Program
Program Analisis Nilai Mahasiswa merupakan program untuk membaca, memvalidasi, dan menganalisis nilai mahasiswa dari file teks. Program dibuat menggunakan Python dengan pembagian beberapa modul agar kode lebih terstruktur dan mudah dipahami.

## 3. Tujuan Program
- Membaca data nama dan nilai mahasiswa dari file teks.
- Memvalidasi nilai dalam rentang 0 sampai 100.
- Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- Menentukan status kelulusan mahasiswa.
- Menampilkan dan menyimpan hasil analisis ke file laporan.

## 4. Fitur Program
1. Membaca data mahasiswa dari `data/nilai_contoh.txt`.
2. Memeriksa format dan validitas data.
3. Menghitung statistik nilai mahasiswa.
4. Menentukan status Lulus atau Tidak Lulus.
5. Menampilkan hasil analisis di terminal.
6. Menyimpan laporan ke `output/hasil_analisis.txt`.
7. Menangani data tidak valid dan file kosong.

## 5. Ketentuan Kelulusan
- Nilai 75 atau lebih: Lulus.
- Nilai di bawah 75: Tidak Lulus.
- Rentang nilai yang diterima: 0 sampai 100.

## 6. Persyaratan
- Python 3.
- Visual Studio Code atau terminal.
- File data dalam format teks dengan susunan Nama,Nilai.

## 7. Cara Menjalankan Program
1. Buka folder proyek di Visual Studio Code.
2. Buka terminal pada folder utama proyek.
3. Jalankan perintah berikut:

   `python src/main.py`

4. Hasil analisis akan ditampilkan di terminal.
5. Laporan tersimpan di folder `output`.

## 8. Struktur Folder
```text
Proyek-Pertemuan-14-2225250165/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    ├── .gitkeep
    └── hasil_analisis.txt
```

## 9. Pengujian Program
Pengujian telah dilakukan terhadap:
- Data normal.
- Nilai batas minimum 0.
- Nilai batas maksimum 100.
- Nilai negatif.
- Nilai di atas 100.
- Nilai bukan angka.
- File kosong.

Seluruh tujuh skenario pengujian yang dijalankan memberikan hasil sesuai harapan. Dokumentasi pengujian dapat dilihat pada `tests/test_case.md`.

## 10. Hasil Program
Berdasarkan data contoh, program menghasilkan:
- Jumlah mahasiswa: 5.
- Rata-rata nilai: 78.00.
- Nilai tertinggi: 90.
- Nilai terendah: 60.
- Jumlah mahasiswa lulus: 4.
- Jumlah mahasiswa tidak lulus: 1.

## 11. Penggunaan AI
AI digunakan sebagai alat bantu untuk memahami konsep pemrograman, menyusun kode, dan memperbaiki dokumentasi. Seluruh kode dan hasil program diperiksa serta diuji kembali.

## 12. Repository GitHub
https://github.com/hanaziyah025-lang/Proyek-Pertemuan-14-2225250165
