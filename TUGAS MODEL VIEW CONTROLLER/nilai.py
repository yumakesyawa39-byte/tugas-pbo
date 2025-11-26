from database import get_connection
from rich import print

class Nilai:
    def __init__(self, siswa, mata_pelajaran, nilai_angka):
        self.siswa = siswa
        self.mata_pelajaran = mata_pelajaran
        self.nilai_angka = nilai_angka

    def tampilkan_nilai(self):
        print("[bold magenta]=== 🧮 Data Nilai Siswa ===[/bold magenta]")
        print(f"[cyan]👤 Nama Siswa     :[/cyan] {self.siswa.nama}")
        print(f"[yellow]📚 Mata Pelajaran :[/yellow] {self.mata_pelajaran.nama_mapel}")
        print(f"[green]🏆 Nilai          :[/green] [bold white]{self.nilai_angka}[/bold white]")
        print("[bold magenta]============================[/bold magenta]")

    def simpan(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO nilai (nis, kode_mapel, nilai) VALUES (?, ?, ?)",
            (self.siswa.nis, self.mata_pelajaran.kode_mapel, self.nilai_angka)
        )
        conn.commit()
        conn.close()
