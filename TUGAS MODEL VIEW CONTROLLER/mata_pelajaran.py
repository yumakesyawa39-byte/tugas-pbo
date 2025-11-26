from database import get_connection

class MataPelajaran:
    def __init__(self, kode_mapel, nama_mapel, sks):
        self.kode_mapel = kode_mapel
        self.nama_mapel = nama_mapel
        self.sks = sks

    def tampilkan_mapel(self):
        print(f"Kode Mapel : {self.kode_mapel}")
        print(f"Nama Mapel : {self.nama_mapel}")
        print(f"SKS        : {self.sks}")

    def simpan(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO mata_pelajaran VALUES (?, ?, ?)",
            (self.kode_mapel, self.nama_mapel, self.sks)
        )
        conn.commit()
        conn.close()
