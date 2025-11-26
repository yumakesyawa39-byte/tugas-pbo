from database import get_connection

class Siswa:
    def __init__(self, nis, nama, jurusan):
        self.nis = nis
        self.nama = nama
        self.jurusan = jurusan

    def tampilkan_data(self):
        print(f"NIS     : {self.nis}")
        print(f"Nama    : {self.nama}")
        print(f"Jurusan : {self.jurusan}")

    def simpan(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO siswa VALUES (?, ?, ?)",
            (self.nis, self.nama, self.jurusan)
        )
        conn.commit()
        conn.close()
