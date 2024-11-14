import socket
import threading
import sqlite3

# Configurazione del server
SERVER_ADDRESS = ('localhost', 12345)
BUFFER_SIZE = 1024

# Funzione per gestire le richieste dei client
def handle_client(client_socket):
    # Connessione al database
    conn = sqlite3.connect('file.db')
    cursor = conn.cursor()

    while True:
        # Ricezione del messaggio dal client
        request = client_socket.recv(BUFFER_SIZE).decode()
        if not request:
            break
        
        # Elaborazione della richiesta
        parts = request.split('|')
        command = parts[0]

        if command == 'CHECK_FILE':
            file_name = parts[1]
            cursor.execute("SELECT * FROM files WHERE nome = ?", (file_name,))
            result = cursor.fetchone()
            if result:
                client_socket.sendall(b'FILE_EXISTS|True')
            else:
                client_socket.sendall(b'FILE_NOT_FOUND|False')

        elif command == 'GET_FRAGMENT_COUNT':
            file_name = parts[1]
            cursor.execute("SELECT tot_frammenti FROM files WHERE nome = ?", (file_name,))
            result = cursor.fetchone()
            if result:
                client_socket.sendall(f'FRAGMENT_COUNT|{result[0]}'.encode())
            else:
                client_socket.sendall(b'ERROR|File non trovato')

        elif command == 'GET_FRAGMENT_IP':
            file_name = parts[1]
            fragment_number = int(parts[2])
            cursor.execute("SELECT host FROM frammenti WHERE id_file = (SELECT id_file FROM files WHERE nome = ?) AND n_frammento = ?", (file_name, fragment_number))
            result = cursor.fetchone()
            if result:
                client_socket.sendall(f'FRAGMENT_IP|{result[0]}'.encode())
            else:
                client_socket.sendall(b'ERROR|Fragmento non trovato')

        elif command == 'GET_ALL_FRAGMENT_IPS':
            file_name = parts[1]
            cursor.execute("SELECT host FROM frammenti WHERE id_file = (SELECT id_file FROM files WHERE nome = ?)", (file_name,))
            results = cursor.fetchall()
            if results:
                ips = ','.join([row[0] for row in results])
                client_socket.sendall(f'ALL_FRAGMENT_IPS|{ips}'.encode())
            else:
                client_socket.sendall(b'ERROR|File non trovato')

    cursor.close()
    conn.close()
    client_socket.close()

# Creazione del server TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(5)
print("Server in ascolto...")

# Ciclo principale per accettare i client
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connessione da {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()