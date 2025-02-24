import socket
import os

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 65536
SAVE_DIR = './synced_files/'

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        request = conn.recv(BUFFER_SIZE).decode()
        print(f"Received message from client: {request}")
        
        if request.startswith("SYNC_REQUEST"):
            try:
                request_parts = request.split()
                if len(request_parts) < 3:
                    conn.send("400 Bad Request".encode())
                    print("Sent response to client: 400 Bad Request")
                    return
                
                file_size = int(request_parts[-1])
                file_name = ' '.join(request_parts[1:-1])
                
                print(f"Preparing to receive file: {file_name} ({file_size} bytes)")

                response = "SYNC_ACK 200 OK"
                conn.send(response.encode())
                
                file_path = os.path.join(SAVE_DIR, file_name)
                with open(file_path, 'wb') as file:
                    received_size = 0
                    while received_size < file_size:
                        chunk = conn.recv(BUFFER_SIZE)
                        if not chunk:
                            break
                        file.write(chunk)
                        received_size += len(chunk)
                        print(f"Receiving {file_name}... {received_size}/{file_size} bytes")

                final_response = "TRANSFER_COMPLETE 201 Created"
                print(f"File '{file_name}' ({file_size} bytes) synced successfully!")
                conn.send(final_response.encode())
            
            except ValueError:
                error_response = "400 Bad Request: Invalid file size"
                conn.send(error_response.encode())
                print(f"Sent response to client: {error_response}")
        
        elif request.startswith("FOLDER_SYNC_REQUEST"):
            folder_path = SAVE_DIR
            
            os.makedirs(folder_path, exist_ok=True)
            
            files = os.listdir(folder_path)
            file_list = "\n".join(files) if files else "No files found"
            
            response = f"FOLDER_SYNC_ACK 200 OK\n{file_list}"
            conn.send(response.encode())
            print(f"Folder '{folder_path}' exists with files:\n{file_list}")

        else:
            error_response = "400 Bad Request"
            conn.send(error_response.encode())
            print(f"Sent response to client: {error_response}")
    
    except Exception as e:
        error_response = f"500 Internal Server Error {e}"
        print(f"Error: {e}")
        conn.send(error_response.encode())
    finally:
        conn.close()
        print(f"Connection with {addr} closed")
        print("-" * 80)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")
        
        while True:
            conn, addr = server_socket.accept()
            handle_client(conn, addr)

if __name__ == "__main__":
    main()
