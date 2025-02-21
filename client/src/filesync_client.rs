use tokio::net::TcpStream;
use tokio::io::{AsyncWriteExt, AsyncReadExt};
use serde_json::json;
use std::fs::File;
use std::io::Read;

#[tokio::main]
async fn main() -> tokio::io::Result<()> {
    let mut stream = TcpStream::connect("127.0.0.1:8484").await?;

    // 1️⃣ อ่านไฟล์
    let filename = "test.txt";
    let mut file = File::open(filename).expect("Failed to open file");
    let mut file_data = Vec::new();
    file.read_to_end(&mut file_data).expect("Failed to read file");

    // 2️⃣ สร้าง JSON Metadata
    let request = json!({
        "command": "UPLOAD_FILE",
        "filename": filename,
        "filesize": file_data.len(),
    });

    // 3️⃣ ส่ง JSON Metadata
    let request_str = request.to_string();
    let request_len = request_str.len() as u32; // ขนาด JSON
    stream.write_all(&request_len.to_be_bytes()).await?; // ✅ ส่งขนาด JSON ก่อน
    stream.write_all(request_str.as_bytes()).await?; // ✅ ส่ง JSON
    stream.flush().await?;

    // 4️⃣ ส่งเนื้อหาไฟล์
    stream.write_all(&file_data).await?;
    stream.flush().await?;

    // 5️⃣ รอรับ Response จาก Server
    let mut buffer = vec![0; 1024];
    let n = stream.read(&mut buffer).await?;
    println!("Response: {:?}", String::from_utf8_lossy(&buffer[..n]));

    Ok(())
}
