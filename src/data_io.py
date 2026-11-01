
def baca_data_nilai(lokasi_file):
    """Membaca dan memvalidasi data nilai dari file teks."""
    daftar_nilai = []

    with open(lokasi_file, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                print(f"Baris {nomor_baris} dilewati: format tidak sesuai.")
                continue

            nama = bagian[0].strip()

            if not nama:
                print(f"Baris {nomor_baris} dilewati: nama kosong.")
                continue

            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor_baris} dilewati: nilai bukan angka.")
                continue

            if nilai < 0 or nilai > 100:
                print(f"Baris {nomor_baris} dilewati: nilai di luar rentang 0-100.")
                continue

            daftar_nilai.append({
                "nama": nama,
                "nilai": nilai
            })

    return daftar_nilai
