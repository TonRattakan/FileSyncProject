use tokio::net::TcpListener;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use serde_json::{Value, json};
use std::fs::OpenOptions;
use std::io::Write;

#[tokio::main]
async fn main() -> tokio::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8484").await?;
    println!("Server is running on 127.0.0.1:8484");

    while let Ok((mut socket, _)) = listener.accept().await {
        tokio::spawn(async move {
            let mut length_buffer = [0u8; 4];
            if socket.read_exact(&mut length_buffer).await.is_err() {
                println!("Failed to read JSON length");
                return;
            }

            let json_len = u32::from_be_bytes(length_buffer) as usize;
            let mut json_buffer = vec![0; json_len];
            if socket.read_exact(&mut json_buffer).await.is_err() {
                println!("Failed to read JSON data");
                return;
            }

            let json_str = String::from_utf8_lossy(&json_buffer);
            let request: Value = match serde_json::from_str(&json_str) {
                Ok(req) => req,
                Err(e) => {
                    println!("Failed to parse JSON: {}", e);
                    return;
                }
            };

            println!("Received: {:?}", request);
            let filename = request["filename"].as_str().unwrap_or("unknown");
            let filesize = request["filesize"].as_u64().unwrap_or(0) as usize;
            println!("📄 Receiving file: {} ({} bytes)", filename, filesize);

            let mut file_data = vec![0; filesize];
            if socket.read_exact(&mut file_data).await.is_err() {
                println!("Failed to read file data");
                return;
            }

            let mut file = OpenOptions::new().create(true).write(true).open(filename).unwrap();
            file.write_all(&file_data).unwrap();

            let response = json!({ "command": "FILE_ACK", "status": "SUCCESS" });
            socket.write_all(response.to_string().as_bytes()).await.unwrap();
        });
    }
    Ok(())
}
