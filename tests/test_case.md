# TEST CASE
## Program Analisis Nilai Mahasiswa

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

### Kesimpulan
Program diharapkan dapat menerima data yang valid, menolak data yang tidak sesuai, serta menampilkan pesan yang jelas ketika terjadi kesalahan.