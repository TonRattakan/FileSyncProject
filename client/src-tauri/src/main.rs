#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::command;
use std::fs::File;
use std::io::{Read, Write};
use std::net::TcpStream;
use serde_json::json;

#[command]
fn upload_file(file_path: String) -> String {
    let mut stream = TcpStream::connect("127.0.0.1:8484").expect("Failed to connect to server");

    let mut file = File::open(&file_path).expect("Failed to open file");
    let mut file_data = Vec::new();
    file.read_to_end(&mut file_data).expect("Failed to read file");

    let filename = file_path.split('/').last().unwrap_or("unknown");
    let request = json!({
        "command": "UPLOAD_FILE",
        "filename": filename,
        "filesize": file_data.len(),
    });

    stream.write_all(request.to_string().as_bytes()).unwrap();
    stream.write_all(b"\n").unwrap();
    stream.write_all(&file_data).unwrap();
    stream.flush().unwrap();

    let mut buffer = vec![0; 1024];
    let n = stream.read(&mut buffer).unwrap();
    let response = String::from_utf8_lossy(&buffer[..n]);

    response.to_string()
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![upload_file])
        .run(tauri::generate_context!())
        .expect("Failed to run Tauri application");
}
