from siswa import Siswa
from mata_pelajaran import MataPelajaran
from nilai import Nilai
from database import init_db
from rich import print

# Inisialisasi SQLite3
init_db()

# objek siswa
siswa1 = Siswa("1001", "Andi Pratama", "Rekayasa Perangkat Lunak")
siswa1.simpan()

# objek mata pelajaran
mapel1 = MataPelajaran("MP01", "Pemrograman Python", 3)
mapel1.simpan()

# objek nilai
nilai1 = Nilai(siswa1, mapel1, 88)
nilai1.simpan()

print("[bold magenta]=== SISTEM NILAI SISWA ===[/bold magenta]")
siswa1.tampilkan_data()
print()
mapel1.tampilkan_mapel()
print()
nilai1.tampilkan_nilai()
