import socket

# Configurazione del client
SERVER_ADDRESS = ('localhost', 12345)
BUFFER_SIZE = 1024

def send_request(request):
    """Invia una richiesta al server e restituisce la risposta."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(SERVER_ADDRESS)
        client_socket.sendall(request.encode())
        response = client_socket.recv(BUFFER_SIZE).decode()
        return response

def main():
    """Funzione principale per gestire il menu del client."""
    while True:
        print("\nMenu:")
        print("1. Controlla se un file esiste")
        print("2. Ottieni il numero di frammenti di un file")
        print("3. Ottieni l'IP di un frammento specifico")
        print("4. Ottieni tutti gli IP dei frammenti di un file")
        print("5. Esci")

        choice = input("Scegli un'opzione (1-5): ")

        if choice == '1':
            file_name = input("Inserisci il nome del file: ")
            response = send_request(f'CHECK_FILE|{file_name}')
            print(response)

        elif choice == '2':
            file_name = input("Inserisci il nome del file: ")
            response = send_request(f'GET_FRAGMENT_COUNT|{file_name}')
            print(response)

        elif choice == '3':
            file_name = input("Inserisci il nome del file: ")
            fragment_number = input("Inserisci il numero del frammento: ")
            response = send_request(f'GET_FRAGMENT_IP|{file_name}|{fragment_number}')
            print(response)

        elif choice == '4':
            file_name = input("Inserisci il nome del file: ")
            response = send_request(f'GET_ALL_FRAGMENT_IPS|{file_name}')
            print(response)

        elif choice == '5':
            print("Uscita dal client.")
            break

        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()