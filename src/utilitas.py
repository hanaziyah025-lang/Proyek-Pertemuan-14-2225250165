
def buat_laporan(hasil):
    """Menyusun hasil analisis menjadi teks laporan."""

    baris_laporan = [
        "===================================",
        "       HASIL ANALISIS NILAI",
        "         MAHASISWA",
        "===================================",
        "",
        "DAFTAR NILAI MAHASISWA:"
    ]

    for nomor, data in enumerate(hasil["mahasiswa"], start=1):
        baris_laporan.append(
            f"{nomor}. {data['nama']} - "
            f"Nilai: {data['nilai']:g} - "
            f"Status: {data['status']}"
        )

    baris_laporan.extend([
        "",
        "RINGKASAN HASIL:",
        f"Rata-rata nilai: {hasil['rata_rata']:.2f}",
        f"Nilai tertinggi: {hasil['nilai_tertinggi']:g}",
        f"Nilai terendah: {hasil['nilai_terendah']:g}",
        f"Jumlah mahasiswa lulus: {hasil['jumlah_lulus']}",
        f"Jumlah mahasiswa tidak lulus: {hasil['jumlah_tidak_lulus']}",
        "",
        "Batas kelulusan: 75",
        "==================================="
    ])

    return "\n".join(baris_laporan)


def simpan_laporan(lokasi_file, isi_laporan):
    """Menyimpan laporan analisis ke file teks."""

    with open(lokasi_file, "w", encoding="utf-8") as file:
        file.write(isi_laporan)
