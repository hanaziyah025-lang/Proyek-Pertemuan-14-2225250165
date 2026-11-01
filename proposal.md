# PROPOSAL PROYEK INDIVIDU
## Program Analisis Nilai Mahasiswa

**Nama:** Hana Karimah Ghoziyah  
**NIM:** 2225250165  
**Kelas:** 3B  
**Mata Kuliah:** Algoritma dan Pemrograman

### 1. Latar Belakang
Pengolahan nilai mahasiswa perlu dilakukan dengan teliti agar hasil perhitungan lebih mudah diketahui. Jika dilakukan secara manual, proses menghitung rata-rata, nilai tertinggi, nilai terendah, dan menentukan kelulusan dapat membutuhkan waktu.

Oleh karena itu, dibuat program Analisis Nilai Mahasiswa untuk membantu mengolah data nilai secara sederhana melalui terminal.

### 2. Pengguna dan Tujuan
Pengguna utama program ini adalah mahasiswa atau pengajar yang ingin mengolah data nilai.

Tujuan program:
- Membaca data nilai mahasiswa.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah mahasiswa yang lulus dan tidak lulus.
- Menampilkan hasil analisis nilai.

### 3. Ruang Lingkup
Program dibuat menggunakan bahasa pemrograman Python dan dijalankan melalui terminal VS Code.

Program dibatasi pada pengolahan data nilai dari file teks. Program tidak menggunakan GUI atau aplikasi berbasis web.

### 4. Kebutuhan Fungsional
1. Membaca data nama dan nilai mahasiswa dari file.
2. Memeriksa apakah data nilai berada pada rentang 0–100.
3. Menghitung nilai rata-rata.
4. Menentukan nilai tertinggi dan terendah.
5. Menentukan status kelulusan.
6. Menampilkan dan menyimpan hasil analisis.

### 5. Kebutuhan Nonfungsional
1. Program dapat dijalankan melalui terminal.
2. Program memiliki pesan kesalahan yang mudah dipahami.
3. Nama variabel dan fungsi mudah dimengerti.
4. Program menggunakan data contoh, bukan data pribadi mahasiswa sebenarnya.

### 6. IPO (Input, Process, Output)

**Input:**
- Nama mahasiswa.
- Nilai mahasiswa dari file teks.

**Process:**
- Membaca data.
- Memvalidasi data nilai.
- Menghitung rata-rata.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah mahasiswa lulus dan tidak lulus.

**Output:**
- Daftar nilai mahasiswa.
- Nilai rata-rata.
- Nilai tertinggi dan terendah.
- Jumlah mahasiswa lulus dan tidak lulus.
- Laporan hasil analisis.

### 7. Algoritma
1. Mulai.
2. Membaca file data nilai mahasiswa.
3. Memeriksa keberadaan dan format file.
4. Memvalidasi setiap data nilai.
5. Menyimpan data yang valid.
6. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
7. Menentukan status kelulusan setiap mahasiswa.
8. Menampilkan hasil analisis.
9. Menyimpan laporan.
10. Selesai.

### 8. Struktur Program
Program dibagi menjadi beberapa file:
- `main.py`: menjalankan program utama.
- `data_io.py`: membaca dan menyimpan data.
- `analisis.py`: melakukan perhitungan dan analisis nilai.
- `utilitas.py`: menyediakan fungsi pendukung.

### 9. Struktur Data
Program menggunakan:
- List untuk menyimpan kumpulan data mahasiswa.
- Dictionary untuk menyimpan nama dan nilai setiap mahasiswa.

### 10. Rencana Pengujian
Pengujian dilakukan menggunakan beberapa kondisi:
1. Data nilai normal.
2. Nilai minimum, yaitu 0.
3. Nilai maksimum, yaitu 100.
4. Nilai di bawah 0.
5. Nilai di atas 100.
6. File data kosong.
7. Format data tidak sesuai.

### 11. Pembagian Tugas
Proyek dikerjakan secara individu. Seluruh kegiatan perancangan, pembuatan program, pengujian, dokumentasi, dan pengelolaan repository dilakukan sendiri.

### 12. Jadwal Pengerjaan
- Pertemuan 14: perancangan proyek dan dokumentasi.
- Pertemuan 15: implementasi, pengujian, dan penyempurnaan program.

### 13. Repository GitHub
https://github.com/hanaziyah025-lang/Proyek-Pertemuan-14-2225250165