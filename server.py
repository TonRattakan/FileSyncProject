import socket
import os
import shlex

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 65536
SAVE_DIR = "synced_files"
LOG_FILE = "server_log.txt"

os.makedirs(SAVE_DIR, exist_ok=True)

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    
    try:
        request = conn.recv(BUFFER_SIZE).decode().strip()
        print(f"Received message from client: {request}")

        if request.startswith("LOG "):
            log_data = request[4:].strip()
            log_message(log_data)
            response = "LOG_ACK 200 OK"
            conn.send(response.encode())
            print(f"[Server] -> {response}")

        elif request.startswith("SYNC_REQUEST"):
            try:
                request_parts = shlex.split(request)
                if len(request_parts) < 3:
                    response = "400 Bad Request"
                    conn.send(response.encode())
                    print(f"[Server] -> {response}")
                    return

                file_size = int(request_parts[-1])
                file_name = request_parts[1]

                print(f"Preparing to receive file: {file_name} ({file_size} bytes)")

                response = "SYNC_ACK 200 OK"
                conn.send(response.encode())
                print(f"[Server] -> {response}")

                file_path = os.path.join(SAVE_DIR, file_name)
                received_size = 0

                with open(file_path, 'wb') as file:
                    while received_size < file_size:
                        chunk = conn.recv(min(BUFFER_SIZE, file_size - received_size))
                        if not chunk:
                            break
                        file.write(chunk)
                        received_size += len(chunk)
                        file.flush()
                        os.fsync(file.fileno())
                        print(f"Receiving {file_name}... {received_size}/{file_size} bytes")

                actual_size = os.path.getsize(file_path)
                print(f"Expected: {file_size}, Received: {received_size}, File size: {actual_size}")

                if received_size == file_size and actual_size == file_size:
                    response = "TRANSFER_COMPLETE 201 Created"
                    conn.send(response.encode())
                    print(f"[Server] -> {response}")
                    print(f"File '{file_name}' received successfully! ({file_size} bytes)")
                else:
                    response = "TRANSFER_FAILED"
                    conn.send(response.encode())
                    print(f"[Server] -> {response}")
                    print(f"[ERROR] File '{file_name}' may be corrupted or incomplete.")

            except ValueError:
                response = "400 Bad Request: Invalid file size"
                conn.send(response.encode())
                print(f"[Server] -> {response}")

        elif request.startswith("FOLDER_SYNC_REQUEST"):
            folder_path = SAVE_DIR
            os.makedirs(folder_path, exist_ok=True)

            files = os.listdir(folder_path)
            file_list = "\n".join(files) if files else "No files found"

            response = f"FOLDER_SYNC_ACK 200 OK\n{file_list}"
            conn.send(response.encode())
            print(f"[Server] -> {response}")

        else:
            response = "400 Bad Request"
            conn.send(response.encode())
            print(f"[Server] -> {response}")

    except Exception as e:
        response = f"500 Internal Server Error {e}"
        print(f"Error: {e}")
        conn.send(response.encode())
        print(f"[Server] -> {response}")

    finally:
        conn.close()
        print(f"Connection with {addr} closed")
        print("-" * 120)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Server started on {HOST}:{PORT}")
        while True:
            conn, addr = server_socket.accept()
            handle_client(conn, addr)

if __name__ == "__main__":
    start_server()
