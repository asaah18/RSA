import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def receive():
    decoded_data = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, address = s.accept()
        with conn:
            print('Connected by', address)
            while True:
                data = conn.recv(2048)
                decoded_data += (data.decode('utf-8'))

                if not data:
                    break
                # conn.sendall(decoded_data)

            print("data= ", decoded_data)
            return decoded_data
