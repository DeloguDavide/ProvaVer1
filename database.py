import sqlite3

# Crea o connette al database SQLite
conn = sqlite3.connect('file.db')
cursor = conn.cursor()

# Creazione della tabella files
cursor.execute('''
CREATE TABLE IF NOT EXISTS files (
    id_file INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    tot_frammenti INTEGER NOT NULL
);
''')

# Creazione della tabella frammenti
cursor.execute('''
CREATE TABLE IF NOT EXISTS frammenti (
    id_frammento INTEGER PRIMARY KEY,
    id_file INTEGER,
    n_frammento INTEGER,
    host TEXT,
    FOREIGN KEY (id_file) REFERENCES files(id_file)
);
''')

# Inserimento di dati di esempio
cursor.execute("INSERT INTO files (nome, tot_frammenti) VALUES ('file1.txt', 3);")
cursor.execute("INSERT INTO frammenti (id_file, n_frammento, host) VALUES (1, 1, '192.168.1.1');")
cursor.execute("INSERT INTO frammenti (id_file, n_frammento, host) VALUES (1, 2, '192.168.1.2');")
cursor.execute("INSERT INTO frammenti (id_file, n_frammento, host) VALUES (1, 3, '192.168.1.3');")

# Salva (commit) le modifiche e chiudi la connessione
conn.commit()
cursor.close()
conn.close()

print("Database creato e dati di esempio inseriti con successo.")