import socket
import threading

HOST = '127.0.0.1'
PORT = 65534

clients = []
usernames = []

def broadcast(message, client_socket=None):
    """Отправка сообщения всем пользователям"""
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client):
    """Обработка сообщений от клиента"""
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} вышел из чата.".encode('utf-8'))
            usernames.remove(username)
            break

def receive_connections():
    """Приём подключений"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Сервер запущен на {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"Подключён {address}")

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Имя пользователя: {username}")
        broadcast(f"{username} присоединился к чату.".encode('utf-8'))
        client.send("Подключено к серверу!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
