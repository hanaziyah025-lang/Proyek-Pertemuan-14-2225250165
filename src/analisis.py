
BATAS_LULUS = 75


def analisis_nilai(daftar_nilai):
    """Menghitung statistik dan status kelulusan mahasiswa."""

    if not daftar_nilai:
        return None

    semua_nilai = [data["nilai"] for data in daftar_nilai]

    rata_rata = sum(semua_nilai) / len(semua_nilai)
    nilai_tertinggi = max(semua_nilai)
    nilai_terendah = min(semua_nilai)

    jumlah_lulus = 0
    jumlah_tidak_lulus = 0
    hasil_mahasiswa = []

    for data in daftar_nilai:
        if data["nilai"] >= BATAS_LULUS:
            status = "Lulus"
            jumlah_lulus += 1
        else:
            status = "Tidak Lulus"
            jumlah_tidak_lulus += 1

        hasil_mahasiswa.append({
            "nama": data["nama"],
            "nilai": data["nilai"],
            "status": status
        })

    return {
        "mahasiswa": hasil_mahasiswa,
        "rata_rata": rata_rata,
        "nilai_tertinggi": nilai_tertinggi,
        "nilai_terendah": nilai_terendah,
        "jumlah_lulus": jumlah_lulus,
        "jumlah_tidak_lulus": jumlah_tidak_lulus
    }
