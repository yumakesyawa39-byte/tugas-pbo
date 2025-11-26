import sqlite3

def get_connection():
    return sqlite3.connect("sekolah.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS siswa (
            nis TEXT PRIMARY KEY,
            nama TEXT,
            jurusan TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mata_pelajaran (
            kode_mapel TEXT PRIMARY KEY,
            nama_mapel TEXT,
            sks INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nis TEXT,
            kode_mapel TEXT,
            nilai INTEGER,
            FOREIGN KEY(nis) REFERENCES siswa(nis),
            FOREIGN KEY(kode_mapel) REFERENCES mata_pelajaran(kode_mapel)
        )
    """)

    conn.commit()
    conn.close()
