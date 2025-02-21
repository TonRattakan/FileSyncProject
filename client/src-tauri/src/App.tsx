import React, { useState } from "react";
const { invoke } = require("@tauri-apps/api/tauri");
const { open } = require("@tauri-apps/api/dialog");

function App() {
  const [file, setFile] = useState<string | null>(null);
  const [status, setStatus] = useState("");

  const selectFile = async () => {
    const selected = await open({
      multiple: false,
      filters: [{ name: "All Files", extensions: ["*"] }],
    });

    if (selected) {
      setFile(selected as string);
    }
  };

  const uploadFile = async () => {
    if (!file) return;
    setStatus("Uploading...");

    try {
      const response = await invoke("upload_file", { filePath: file });
      setStatus(`Upload success: ${response}`);
    } catch (error) {
      setStatus(`Error: ${error}`);
    }
  };

  return (
    <div style={{ padding: "20px", textAlign: "center" }}>
      <h1>FileSync</h1>
      <button onClick={selectFile}>Select File</button>
      {file && <p>Selected: {file}</p>}
      <button onClick={uploadFile} disabled={!file}>Upload</button>
      <p>{status}</p>
    </div>
  );
}

export default App;
