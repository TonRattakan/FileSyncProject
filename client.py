import socket
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 65536
LOCAL_SAVE_DIR = './synced_files/'

if not os.path.exists(LOCAL_SAVE_DIR):
    os.makedirs(LOCAL_SAVE_DIR)

class FileSyncClient:
    def __init__(self, root):
        self.root = root
        self.root.title("FileSyncNet Client")

        self.file_path = tk.StringVar()
        self.folder_path = tk.StringVar()
        self.new_file_name = tk.StringVar()
        self.new_file_content = tk.StringVar()

        # File Sync UI
        tk.Label(root, text="Select File to Sync:").pack(pady=5)
        tk.Entry(root, textvariable=self.file_path, width=50).pack(padx=10, pady=5)
        tk.Button(root, text="Browse File", command=self.browse_file).pack(pady=5)
        tk.Button(root, text="Sync File", command=self.start_sync_thread).pack(pady=10)

        # Folder Sync UI
        tk.Label(root, text="Select Folder to Sync:").pack(pady=5)
        tk.Entry(root, textvariable=self.folder_path, width=50).pack(padx=10, pady=5)
        tk.Button(root, text="Browse Folder", command=self.browse_folder).pack(pady=5)
        tk.Button(root, text="Sync Folder", command=self.start_sync_folder_thread).pack(pady=10)

        # File Creation UI
        tk.Label(root, text="Create New Text File:").pack(pady=5)
        # Entry for file name
        self.entry_file_name = tk.Entry(root, textvariable=self.new_file_name, width=50, fg="gray")
        self.entry_file_name.pack(padx=10, pady=5)

        # Add placeholder effect
        self.entry_file_name.insert(0, "Enter file name...")
        self.entry_file_name.bind("<FocusIn>", self.clear_placeholder)
        self.entry_file_name.bind("<FocusOut>", self.add_placeholder)

        self.text_area = tk.Text(root, height=5, width=50)
        self.text_area.pack(padx=10, pady=5)
        tk.Button(root, text="Save File", command=self.create_file).pack(pady=5)

        self.status_label = tk.Label(root, text="Status: Idle", fg="blue")
        self.status_label.pack(pady=5)

    def browse_file(self):
        file = filedialog.askopenfilename()
        self.file_path.set(file)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        self.folder_path.set(folder)

    def start_sync_thread(self):
        threading.Thread(target=self.sync_file, daemon=True).start()

    def start_sync_folder_thread(self):
        threading.Thread(target=self.sync_folder, daemon=True).start()

    def clear_placeholder(self, event):
        if self.entry_file_name.get() == "Enter file name...":
            self.entry_file_name.delete(0, tk.END)
            self.entry_file_name.config(fg="black")

    def add_placeholder(self, event):
        if not self.entry_file_name.get():
            self.entry_file_name.insert(0, "Enter file name...")
            self.entry_file_name.config(fg="gray")


    def create_file(self):
        file_name = self.new_file_name.get().strip()
        file_content = self.text_area.get("1.0", tk.END).strip()

        if not file_name:
            messagebox.showwarning("Warning", "Please enter a file name")
            return

        if not file_name.endswith(".txt"):
            file_name += ".txt"

        file_path = os.path.join(LOCAL_SAVE_DIR, file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(file_content)

            messagebox.showinfo("Success", f"File '{file_name}' created successfully!")
            self.status_label.config(text=f"Status: File '{file_name}' saved", fg="green")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to create file: {e}")
            self.status_label.config(text="Status: Error", fg="red")

    def sync_file(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showwarning("Warning", "Please select a file")
            return

        file_size = os.path.getsize(file_path)
        print(f"Starting sync: {os.path.basename(file_path)} ({file_size} bytes)")

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                file_name = os.path.basename(file_path)

                s.send(f"SYNC_REQUEST {file_name} {file_size}".encode())
                response = s.recv(BUFFER_SIZE).decode()

                if "SYNC_ACK" in response:
                    with open(file_path, 'rb') as file:
                        sent_size = 0
                        while chunk := file.read(BUFFER_SIZE):
                            s.send(chunk)
                            sent_size += len(chunk)
                            print(f"Sending {file_name}... {sent_size}/{file_size} bytes")

                    final_response = s.recv(BUFFER_SIZE).decode()
                    if "TRANSFER_COMPLETE" in final_response:
                        print(f"File '{file_name}' successfully sent ({file_size} bytes)")
                        print("-" * 80)
                        self.status_label.config(text="Status: File Synced Successfully", fg="green")
                    else:
                        print("-" * 80)
                        self.status_label.config(text="Status: Sync Failed", fg="red")
                else:
                    self.status_label.config(text="Status: Sync Rejected", fg="red")
        except Exception as e:
            self.status_label.config(text=f"Status: Error - {e}", fg="red")

    def sync_folder(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            messagebox.showwarning("Warning", "Please select a folder")
            return

        try:
            files = os.listdir(folder_path)
            if not files:
                messagebox.showwarning("Warning", "Folder is empty")
                return

            for file_name in files:
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    self.file_path.set(file_path)
                    self.sync_file()

            self.status_label.config(text="Status: Folder Synced Successfully", fg="green")

        except Exception as e:
            self.status_label.config(text=f"Status: Error - {e}", fg="red")

def main():
    root = tk.Tk()
    client = FileSyncClient(root)
    root.mainloop()

if __name__ == "__main__":
    main()
