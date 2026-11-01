
from pathlib import Path

from data_io import baca_data_nilai
from analisis import analisis_nilai
from utilitas import buat_laporan, simpan_laporan


# Menentukan lokasi folder utama proyek
FOLDER_PROYEK = Path(__file__).resolve().parent.parent

# Menentukan lokasi file input dan output
FILE_INPUT = FOLDER_PROYEK / "data" / "nilai_contoh.txt"
FILE_OUTPUT = FOLDER_PROYEK / "output" / "hasil_analisis.txt"


def main():
    """Menjalankan seluruh proses analisis nilai mahasiswa."""

    print("PROGRAM ANALISIS NILAI MAHASISWA")
    print("===================================")

    try:
        daftar_nilai = baca_data_nilai(FILE_INPUT)

        if not daftar_nilai:
            print("Tidak ada data nilai yang valid untuk dianalisis.")
            return

        hasil = analisis_nilai(daftar_nilai)
        laporan = buat_laporan(hasil)

        print()
        print(laporan)

        simpan_laporan(FILE_OUTPUT, laporan)

        print()
        print(f"Laporan berhasil disimpan di: {FILE_OUTPUT}")

    except FileNotFoundError:
        print("File data tidak ditemukan. Periksa kembali lokasi file input.")
    except OSError as error:
        print(f"Terjadi kesalahan saat mengakses file: {error}")


if __name__ == "__main__":
    main()
