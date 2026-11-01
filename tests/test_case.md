# Program Analisis Nilai Mahasiswa

Pengujian dilakukan untuk memastikan program dapat membaca, memvalidasi, dan menganalisis data nilai mahasiswa dengan benar.

### 1. Test Case Normal

| No. | Data Masukan | Hasil yang Diharapkan |
|---|---|---|
| 1 | Andi,80 | Data diterima dan nilai berhasil dianalisis |
| 2 | Budi,90 | Data diterima dan nilai berhasil dianalisis |

### 2. Test Case Batas

| No. | Data Masukan | Hasil yang Diharapkan |
|---|---|---|
| 3 | Citra,0 | Nilai diterima karena merupakan batas minimum |
| 4 | Dinda,100 | Nilai diterima karena merupakan batas maksimum |
| 5 | Nilai 74 | Status Tidak Lulus karena di bawah batas kelulusan |
| 6 | Nilai 75 | Status Lulus karena memenuhi batas kelulusan |

### 3. Test Case Tidak Valid

| No. | Data Masukan | Hasil yang Diharapkan |
|---|---|---|
| 7 | Eko,-5 | Data ditolak karena nilai kurang dari 0 |
| 8 | Fani,110 | Data ditolak karena nilai lebih dari 100 |
| 9 | Gita,abc | Data ditolak karena nilai bukan angka |
| 10 | File kosong | Program menampilkan pesan bahwa tidak ada data yang dapat dianalisis |

### 4. Kesimpulan

Program diharapkan dapat menerima data yang valid, menolak data yang tidak sesuai, serta menampilkan pesan yang jelas ketika terjadi kesalahan.

## 5. Hasil Pengujian Program

| No. | Jenis Pengujian | Data Masukan | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Normal | Andi,80; Budi,90; Citra,75; Dinda,60; Eko,85 | Rata-rata 78.00, 4 lulus, 1 tidak lulus | Sesuai harapan | Berhasil |
| 2 | Batas minimum | Citra,0 | Data diterima, status Tidak Lulus | Data diterima, status Tidak Lulus | Berhasil |
| 3 | Batas maksimum | Dinda,100 | Data diterima, status Lulus | Data diterima, status Lulus | Berhasil |
| 4 | Nilai negatif | Eko,-5 | Data ditolak | Data dilewati | Berhasil |
| 5 | Nilai di atas 100 | Fani,110 | Data ditolak | Data dilewati | Berhasil |
| 6 | Nilai bukan angka | Gita,abc | Data ditolak | Data dilewati | Berhasil |
| 7 | Data kosong | File tanpa isi | Program menampilkan pesan bahwa tidak ada data valid | Pesan ditampilkan tanpa error | Berhasil |
| 8 | Batas kelulusan | Citra,74 | Status Tidak Lulus | Status Tidak Lulus | Berhasil |
| 9 | File tidak ditemukan | File input diubah namanya sementara | Program menampilkan pesan file tidak ditemukan | Pesan file tidak ditemukan ditampilkan tanpa error | Berhasil |

## 6. Kesimpulan Pengujian

Berdasarkan pengujian yang telah dilakukan, program dapat membaca data nilai mahasiswa, memvalidasi nilai dalam rentang 0 sampai 100, menghitung hasil analisis, menentukan status kelulusan, dan menyimpan laporan. Program juga dapat menangani data tidak valid, file kosong, dan file yang tidak ditemukan tanpa mengalami error. Seluruh sembilan skenario pengujian yang dicatat pada bagian hasil pengujian memberikan hasil sesuai harapan.