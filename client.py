import socket

# Configurazione del client
SERVER_ADDRESS = ('localhost', 12345)
BUFFER_SIZE = 1024

def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(SERVER_ADDRESS)
        client_socket.sendall(request.encode())
        response = client_socket.recv(BUFFER_SIZE).decode()
        return response

# Esempi di richieste
if __name__ == "__main__":
    # Controlla se un file esiste
    response = send_request('CHECK_FILE|dune.mov')
    print(response)

    # Ottieni il numero di frammenti di un file
    response = send_request('GET_FRAGMENT_COUNT|dune.mov')
    print(response)

    # Ottieni l'IP di un frammento specifico
    response = send_request('GET_FRAGMENT_IP|dune.mov|1')
    print(response)

    # Ottieni tutti gli IP dei frammenti di un file
    response = send_request('GET_ALL_FRAGMENT_IPS|dune.mov')
    print(response)

    print("---------------")

    response = send_request('CHECK_FILE|ciclofondazione_asimov.djvu')
    print(response)

    # Ottieni il numero di frammenti di un file
    response = send_request('GET_FRAGMENT_COUNT|ciclofondazione_asimov.djvu')
    print(response)

    # Ottieni l'IP di un frammento specifico
    response = send_request('GET_FRAGMENT_IP|ciclofondazione_asimov.djvu|1')
    print(response)

    # Ottieni tutti gli IP dei frammenti di un file
    response = send_request('GET_ALL_FRAGMENT_IPS|ciclofondazione_asimov.djvu')
    print(response)

    print("---------------")

    response = send_request('CHECK_FILE|whatif_munroe.epub')
    print(response)

    # Ottieni il numero di frammenti di un file
    response = send_request('GET_FRAGMENT_COUNT|whatif_munroe.epub')
    print(response)

    # Ottieni l'IP di un frammento specifico
    response = send_request('GET_FRAGMENT_IP|whatif_munroe.epub|1')
    print(response)

    # Ottieni tutti gli IP dei frammenti di un file
    response = send_request('GET_ALL_FRAGMENT_IPS|whatif_munroe.epub')
    print(response)